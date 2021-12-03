import os, sys

file_name = 'input_day_7.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line.split(' bags contain ') for line in f.read().split('\n') if line != ''] 

    def parse_rule(rule):
        outer_bag = rule[0]
        if 'no other' in rule[1]: 
            return [(outer_bag, 0, '')]
        inner_bags = rule[1].replace('bags','').replace('bag','').replace('.','').split(', ')
        return [(outer_bag, int(bag.split()[0]), ' '.join(bag.split()[1:])) for bag in inner_bags]

    lst = [parse_rule(rule) for rule in lst]
    lst = [rule for sublist in lst for rule in sublist]
    
    def list_children(bag):
        ans = []
        for rule in lst:
            if rule[0] != bag or rule[1] == 0: continue
            ans += [rule[2]] + list_children(rule[2])
        return ans
    
    d = {bag: list_children(bag) for bag in set([rule[0] for rule in lst])}
    
    ans1 = sum(1 for bag, inner_bags in d.items() if 'shiny gold' in inner_bags)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    def count_children(bag):
        ans = 0
        for rule in lst:
            if rule[0] != bag or rule[1] == 0: continue
            ans += rule[1] 
            ans += count_children(rule[2]) * rule[1]
        return ans
    
    ans2 = count_children('shiny gold')
    print(f'answer to second puzzle of day {day} is: {ans2}')

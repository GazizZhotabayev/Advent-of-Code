import os, sys, re
from functools import reduce

file_name = 'input_day_19.txt'
file_name = 'input_day_19_2.txt'
#file_name = 'test_19.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    rules, msgs = f.read().split('\n\n')
    rules, msgs = rules.split('\n'), msgs.split('\n')
    RULES = {rule.split(': ')[0]: rule.split(': ')[1].replace('"','') for rule in rules}
    
    collate = lambda lst: reduce(lambda x, y: x + y, lst) 

    def parse_rule(rule):
        if all(c.isalpha() or c in '(|)' for c in rule):
            return rule
        if '|' in rule:
            p1, p2 = rule.split(' | ')
            return '(' + parse_rule(p1) + '|' + parse_rule(p2) + ')'
        else:
            return collate([parse_rule(RULES[r]) for r in rule.split()])
        
    rule_0 = parse_rule(RULES['0'])
    pattern = re.compile(f'^{rule_0}$')
    ans1 = 0
    for msg in msgs:
        if pattern.match(msg): 
            ans1 += 1
    
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = 0
    for msg in msgs:
        if pattern.match(msg): 
            ans2 += 1

    print(f'answer to second puzzle of day {day} is: {ans2}')
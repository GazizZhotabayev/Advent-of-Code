import os, sys
from collections import Counter

file_name = 'input_day_14.txt'
file_name = 'test_14.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    LINE, rules = f.read().split('\n\n')
    rules = rules.split('\n')

    def parse_rule(rule):
       p1, p2 = rule.split(' -> ') 
       return p1[0]+p2

    RULES = {rule.split(' -> ')[0]: parse_rule(rule) for rule in rules}

    def step(line):
        return ''.join(RULES.get(c + line[i+1]) for i, c in enumerate(line[:-1])) + line[-1]

    for i in range(10):
        print(LINE[:100])
        LINE = step(LINE)
        
        #c = sorted([v for k, v in Counter(LINE).items()])
        #print(c[-1] - c[0])
        #print(Counter(LINE))

    c = sorted([v for k, v in Counter(LINE).items()])
    ans1 = c[-1] - c[0]
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = 0
    print(f'answer to second puzzle of day {day} is: {ans2}')

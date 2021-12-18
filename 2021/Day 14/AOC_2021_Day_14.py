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

    line = LINE
    for i in range(10):
        #print(LINE[:100])
        line = step(line)
        
        #c = sorted([v for k, v in Counter(LINE).items()])
        #print(c[-1] - c[0])
        #c = Counter(LINE)
        #min_c, max_c, sum_c = min(c.values()), max(c.values()), sum(c.values())
        #print(float(min_c / sum_c), float(max_c / sum_c), sum_c)

    c = sorted([v for k, v in Counter(line).items()])
    ans1 = c[-1] - c[0]
    print(f'answer to first puzzle of day {day} is: {ans1}')

    SOLUTION = {letter: 0 for letter in set(LINE)}
    COUNTERS = {}
    for rule in RULES:
        line = rule
        for i in range(20):
            line = step(line)
        COUNTERS[rule] = Counter(line)

    line = LINE
    for i in range(20):
        line = step(line)
        pairs = [''.join(line[i:i+2]) for i in range(len(line)-1)]
        PAIRS_COUNTER = Counter(pairs)
        print(PAIRS_COUNTER)

    ans2 = 0
    print(f'answer to second puzzle of day {day} is: {ans2}')

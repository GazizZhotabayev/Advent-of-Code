import os, sys
from collections import Counter

file_name = 'input_day_14.txt'
#file_name = 'test_14.txt'
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
        line = step(line)

    c = Counter(line)
    ans1 = max(c.values()) - min(c.values())
    print(f'answer to first puzzle of day {day} is: {ans1}')

    SOLUTION = {letter: 0 for letter in set(''.join(RULES.keys()))}
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
    
    for pair, pair_cnt in PAIRS_COUNTER.items():
        for letter, letter_cnt in COUNTERS[pair].items():
            SOLUTION[letter] += pair_cnt * letter_cnt
            if pair[0] == letter:
                SOLUTION[letter] -= pair_cnt

    ans2 = max(SOLUTION.values()) - min(SOLUTION.values()) + 1
    print(f'answer to second puzzle of day {day} is: {ans2}')

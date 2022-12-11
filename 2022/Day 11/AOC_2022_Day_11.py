import os, sys
from operator import mul
from functools import reduce

file_name = 'input.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    instructions = f.read().split('\n\n')

empty = {s: '' for s in 'items operation test if_true if_false cnt'.split()}
MONKEYS = {i:empty.copy() for i in range(len(instructions))}

def parse(instruction, MONKEYS):
    instruction = instruction.split('\n')
    n = int(''.join(i for i in instruction[0] if i.isnumeric()))
    MONKEYS[n]['items'] = [int(i) for i in instruction[1].split(': ')[-1].split(', ')]
    MONKEYS[n]['operation'] = lambda old: eval(instruction[2].split(' = ')[-1])
    MONKEYS[n]['divisor'] = int(instruction[3].split(' by ')[-1])
    MONKEYS[n]['test'] = lambda x : x % MONKEYS[n]['divisor'] == 0
    MONKEYS[n]['if_true'] = int(instruction[4].split('monkey ')[-1])
    MONKEYS[n]['if_false'] = int(instruction[5].split('monkey ')[-1])
    MONKEYS[n]['cnt'] = 0

for instruction in instructions: parse(instruction, MONKEYS)

def play_round(MONKEYS, divisor, modulo):
    for monkey in range(len(MONKEYS)):
        while len(MONKEYS[monkey]['items']) > 0:
            item = MONKEYS[monkey]['items'].pop(0)
            item = MONKEYS[monkey]['operation'](item)
            item = item // divisor
            item = item % modulo
            test = MONKEYS[monkey]['test'](item)
            if test:
                n = MONKEYS[monkey]['if_true']
            else:
                n = MONKEYS[monkey]['if_false']
            MONKEYS[n]['items'].append(item)
            MONKEYS[monkey]['cnt'] += 1
            #print(f'item with worry level {item} is thrown to monkey {n}')

product = lambda x: reduce(mul, x, 1)
m = product([MONKEYS[i]['divisor'] for i in range(len(MONKEYS))])

#for round in range(20):
#    play_round(MONKEYS, 3, m)

for round in range(10000):
    play_round(MONKEYS, 1, m)

    #print(f'\nafter round {round+1}:')
    #for monkey in range(len(MONKEYS)):
    #    items = MONKEYS[monkey]['items']
    #    print(f'Monkey {monkey}: {items}')

counts = sorted([MONKEYS[i]['cnt'] for i in range(len(MONKEYS))])
ans = counts[-1] * counts[-2]
print(f'answer is: {ans}')
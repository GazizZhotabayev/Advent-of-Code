import os, sys
from itertools import accumulate

file_name = 'input.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    instructions = f.read().split('\n')

N = [1]
for i in range(len(instructions) + 1):
    if i < len(instructions):
        instruction = instructions[i]
        if instruction == 'noop':
            N += [0]
        else:
            n = int(instruction.split()[-1])
            N += [0, n]

X = list(accumulate(N))

ans1 = sum([X[i-1] * i for i in range(20, 221, 40)])
print(f'answer to first puzzle is: {ans1}')

screen = list('.' * 240)
for i, x in enumerate(X):
    if i % 40 in range(x-1, x+2):
        screen[i] = '#'

screen = [screen[i:i+40] for i in range(0, len(screen), 40)]
print('\n'.join(''.join(line) for line in screen))
import os, sys

file_name = 'input.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    stacks, instructions = f.read().split('\n\n') 

stacks = stacks.split('\n')
stacks = list(map(list, zip(*stacks)))
stacks = [stacks[i][:-1] for i in range(1, len(stacks), 4)]
stacks = [[x for x in stack if x.isalpha()] for stack in stacks]
instructions = instructions.split('\n')

def parse(instruction, cratemover):
    n, from_stack, to_stack = [int(i) for i in instruction.split() if i.isnumeric()]
    from_stack -= 1
    to_stack -= 1
    if cratemover == 9000: crates = stacks[from_stack][:n][::-1]
    if cratemover == 9001: crates = stacks[from_stack][:n]
    stacks[from_stack] = stacks[from_stack][n:]
    stacks[to_stack] = crates + stacks[to_stack]

#for instruction in instructions: parse(instruction, 9000)
#ans1 = ''.join(stacks[i][0] for i in range(len(stacks)))
#print(f'answer to first puzzle of day {day} is: {ans1}')

for instruction in instructions: parse(instruction, 9001)
ans2 = ''.join(stacks[i][0] for i in range(len(stacks)))
print(f'answer to second puzzle of day {day} is: {ans2}')
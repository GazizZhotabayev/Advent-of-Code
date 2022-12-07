import os, sys

file_name = 'input.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    instructions = f.read().split('\n')

directories = dict()

def parse(instruction, current_dir):
    if instruction.startswith('$ cd'):
        directory = instruction.split()[-1]
        if directory == '..':
            current_dir = '-'.join(current_dir.split('-')[:-1])
        elif directory == '/':
            current_dir = '/'
        else:
            current_dir = current_dir + '-' + directory
    else:
        if instruction.startswith('$ ls'): return current_dir
        x, y = instruction.split()
        if x.isnumeric():
            if current_dir in directories:
                directories[current_dir] += [(x, y)]
            else:
                directories[current_dir] = [(x, y)]
        else:
            y = current_dir + '-' + y
            if current_dir in directories:
                directories[current_dir] += [y]
            else:
                directories[current_dir] = [y]
    return current_dir

current_dir = '/'
for instruction in instructions: 
    current_dir = parse(instruction, current_dir)

directory_sizes = dict()
def size(directory):
    s = 0
    for element in directories[directory]:
        if isinstance(element, tuple):
            s += int(element[0])
        else:
            try:
                s += directory_sizes[element]
            except:
                return
    directory_sizes[directory] = s

while len(directory_sizes) < len(directories):
    for directory in directories:
        size(directory)

ans1 = sum(v for k, v in directory_sizes.items() if v <= 100000)
print(f'answer to first puzzle of day {day} is: {ans1}')

used_space = directory_sizes['/']
unused_space = 70000000 - used_space
gap = 30000000 - unused_space

ans2 = min(v for k, v in directory_sizes.items() if v >= gap)
print(f'answer to second puzzle of day {day} is: {ans2}')
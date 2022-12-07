import os, sys

file_name = 'input_day_1.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [sum([int(line) for line in section.split('\n')]) for section in f.read().split('\n\n')] 

print(f'answer to first puzzle is: {max(lst)}')

print(f'answer to second puzzle is: {sum(sorted(lst)[-3:])}')
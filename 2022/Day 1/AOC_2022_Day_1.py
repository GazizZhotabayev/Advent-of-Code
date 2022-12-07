import os, sys

file_name = 'input_day_1.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [sum([int(line) for line in section.split('\n')]) for section in f.read().split('\n\n')] 

print(f'answer to first puzzle of day {day} is: {max(lst)}')

print(f'answer to second puzzle of day {day} is: {sum(sorted(lst)[-3:])}')
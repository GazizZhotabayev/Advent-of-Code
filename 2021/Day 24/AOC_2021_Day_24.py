import os, sys

file_name = 'input_day_24.txt'
file_name = 'test_24.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:

    INSTRUCTIONS = [parse(line) for line in f.read().split('\n')]

    ans1 = 0
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = 0
    print(f'answer to second puzzle of day {day} is: {ans2}')

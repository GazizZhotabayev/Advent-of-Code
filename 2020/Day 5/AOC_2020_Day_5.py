import os, sys

file_name = 'input_day_5.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [(line[:7].replace('F','0').replace('B','1'), line[7:].replace('R','1').replace('L','0')) for line in f.read().split('\n') if line != ''] 
    lst = [int(row, 2) * 8 + int(column, 2) for row, column in lst]

    print(f'answer to first puzzle of day {day} is: {max(lst)}')

    print(f'answer to second puzzle of day {day} is: {max(set(range(max(lst))) - set(lst))}')

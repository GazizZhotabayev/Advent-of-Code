import os, sys

file_name = 'input_day_2.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line.replace(':','').split() for line in f.read().split('\n') if line != ''] 
    lst = [[int(i) for i in line[0].split('-')] + line[1:] for line in lst]

    ans1 = sum(line[3].count(line[2]) in range(line[0], line[1]+1) for line in lst)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    print(lst[:2])
    ans2 = sum((line[3][line[0]-1]+line[3][line[1]-1]).count(line[2]) == 1 for line in lst)
    print(f'answer to second puzzle of day {day} is: {ans2}')
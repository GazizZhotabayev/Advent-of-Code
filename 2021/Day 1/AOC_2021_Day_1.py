import os, sys

file_name = 'input_day_1.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    #parse the .txt into a list of integers
    lst1 = [int(line) for line in f.read().split('\n') if line != ''] 

#f will count the # of times there was an increase in consecutive numbers of a list
f = lambda lst: sum(1 if lst[i+1] > e else 0 for i, e in enumerate(lst[:-1]))

print(f'answer to first puzzle of day {day} is: {f(lst1)}')

#transform the list to a rolling 3 window
lst2 = [sum(lst1[i:i+3]) for i, e in enumerate(lst1[:-2])]

print(f'answer to second puzzle of day {day} is: {f(lst2)}')

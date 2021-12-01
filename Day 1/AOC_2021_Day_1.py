import os, sys

file_name = 'input_day_1.txt'
with open(os.path.join(sys.path[0], file_name)) as f:
    #parse the .txt into a list of integers
    lst1 = [int(i) for i in f.read().split('\n') if i != ''] 

#f will count the # of times there was an increase in consecutive numbers of a list
f = lambda lst: sum(1 if lst[i+1] > e else 0 for i, e in enumerate(lst[:-1]))

print(f'answer to first puzzle of day 1 is: {f(lst1)}')

#transform the list to a rolling 3 window
lst2 = [sum(lst1[i:i+3]) for i, e in enumerate(lst1[:-2])]

print(f'answer to second puzzle of day 1 is: {f(lst2)}')

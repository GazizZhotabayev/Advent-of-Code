import os, sys
from functools import reduce

file_name = 'input_day_6.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line.split('\n') for line in f.read()[:-1].split('\n\n') if line != ''] 
    
    collate = lambda x: reduce(lambda l1, l2: l1+l2, x)
    ans1 = [len(set(collate(group))) for group in lst]
    print(f'answer to first puzzle of day {day} is: {sum(ans1)}')

    intersection = lambda x: ''.join(sorted(reduce(lambda l1, l2: set(l1).intersection(set(l2)), x)))
    ans2 = [intersection(group) for group in lst]
    print(f'answer to second puzzle of day {day} is: {sum([len(i) for i in ans2])}')
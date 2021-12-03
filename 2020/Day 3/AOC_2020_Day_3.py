import os, sys
from functools import reduce

file_name = 'input_day_3.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line * 100 for line in f.read().split('\n') if line != ''] 

def num_trees(x, right, down):
    rows, cols = len(x), len(x[0])
    
    i, j, counter = 0, 1, 0
    while i < rows-1:
        i += down
        j += right
        if x[i][j-1] == '#': counter += 1
        
    return counter

ans = [num_trees(lst, i, j) for i, j in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]

print(f'answer to first puzzle of day {day} is: {ans[1]}')

print(f'answer to second puzzle of day {day} is: {reduce(lambda x, y: x*y, ans)}')
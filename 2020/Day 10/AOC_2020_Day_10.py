import os, sys
from functools import reduce

file_name = 'input_day_10.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [int(line) for line in f.read().split('\n') if line != ''] 
    x = []
    for n in lst: x += list(range(n-3, n))
    lst += x + [0, max(lst) + 3]

    print(lst[:10])
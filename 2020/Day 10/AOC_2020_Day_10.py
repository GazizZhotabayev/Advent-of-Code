import os, sys

file_name = 'input_day_10.txt'
#file_name = 'test_10.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [int(line) for line in f.read().split('\n') if line != ''] 
    lst += [0, max(lst) + 3]

    lst = [i for i in sorted(set(lst)) if i >= 0]
    gaps = [n-lst[i] for i, n in enumerate(lst[1:])]

    ans1 = gaps.count(3) * gaps.count(1)
    print(f'answer to first puzzle of day {day} is: {ans1}')
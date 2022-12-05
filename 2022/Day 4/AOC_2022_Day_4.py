import os, sys

file_name = 'input.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    #parse the .txt into a list of integers
    lst = [line.split(',') for line in f.read().split('\n')] 

lst = [[sub.split('-') for sub in line] for line in lst]
lst = [[[int(i) for i in sub] for sub in line] for line in lst]

ans1, ans2 = 0, 0
for pair in lst:
    a, b = pair[0]
    x, y = pair[1]
    if (a <= x and b >= y) or (a >= x and b <= y):
        ans1 += 1
    if (a <= y and b >= x) or (a >= y and b <= x):
        ans2 += 1

print(f'answer to first puzzle of day {day} is: {ans1}')

print(f'answer to second puzzle of day {day} is: {ans2}')
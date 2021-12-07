import os, sys

file_name = 'input_day_7.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    crabs = [int(i) for i in f.read().split(',')]

    gaps = lambda lst, pos: sum(abs(x-pos) for i, x in enumerate(lst))

    ans1 = min([gaps(crabs, i) for i in range(min(crabs), max(crabs) + 1)])
    print(f'answer to first puzzle of day {day} is: {ans1}')

    sum_to_n = lambda n: (n * (n+1)) // 2
    gaps2 = lambda lst, pos: sum(sum_to_n(abs(x-pos)) for i, x in enumerate(lst))
    ans2 = min([gaps2(crabs, i) for i in range(min(crabs), max(crabs) + 1)])
    print(f'answer to second puzzle of day {day} is: {ans2}')
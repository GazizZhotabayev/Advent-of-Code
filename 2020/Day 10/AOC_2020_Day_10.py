import os, sys
from functools import reduce

file_name = 'input_day_10.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [int(line) for line in f.read().split('\n') if line != ''] 
    lst += [0, max(lst) + 3]
    lst = [i for i in sorted(set(lst)) if i >= 0]
    gaps = [n-lst[i] for i, n in enumerate(lst[1:])]

    ans1 = gaps.count(3) * gaps.count(1)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    def num_paths(x):
        if len(x) <= 2: return 1
        return sum(num_paths(x[i:]) for i in range(1,4) if 0 < i <= len(x)-1 and x[i]-x[0] <= 3)

    def split_list(x):
        ans, last = [[]], None
        for e in x:
            if last is None or abs(last - e) < 3:
                ans[-1].append(e)
            else:
                ans.append([e])
            last = e 
        return ans

    ans2 = reduce(lambda x, y: x*y, [num_paths(sublist) for sublist in split_list(lst)])
    print(f'answer to second puzzle of day {day} is: {ans2}')
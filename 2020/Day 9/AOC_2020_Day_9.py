import os, sys

file_name = 'input_day_9.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [int(line) for line in f.read().split('\n') if line != ''] 

    def sum_in_list(x, n):
        for i in x:
            if i != n-i and i in x and (n-i) in x:
                return True
        return False

    gap = 25
    for i, n in enumerate(lst):
        if i < gap: continue
        x = lst[i-gap:i][:]
        if not sum_in_list(x, n):
            break
    
    ans1 = n
    print(f'answer to first puzzle of day {day} is: {ans1}')

    for i, n in enumerate(lst):
        j, x = i, []
        while sum(x) < ans1:
            x += [lst[j]]
            j += 1
        
        if sum(x) == ans1: break
    
    print(i, sum(x))
    ans2 = max(x) + min(x)
    print(f'answer to second puzzle of day {day} is: {ans2}')
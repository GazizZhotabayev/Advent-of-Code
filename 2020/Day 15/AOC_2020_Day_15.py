import os, sys

file_name = 'input_day_15.txt'
day = file_name.split('.')[0].split('_')[-1]

last_index = lambda arr, x: len(arr) - arr[::-1].index(x) - 1

def spoken_number(lst, n):
    tracker = {e: last_index(lst[:-1], e) for e in lst[:-1]}
    
    for turn in range(n-1):
        if turn < len(lst)-1: continue
        
        x = lst[turn]
        if x in tracker:
            lst += [turn - tracker[x]]
        else:
            lst += [0]
        
        tracker[x] = turn
        
    return lst[-1]

ans1 = spoken_number([1,20,11,6,12,0], 2020)
print(f'answer to first puzzle of day {day} is: {ans1}')

ans2 = spoken_number([1,20,11,6,12,0], 30000000)
print(f'answer to second puzzle of day {day} is: {ans2}')

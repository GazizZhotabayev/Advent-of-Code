import os, sys

file_name = 'input_day_1.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [int(line) for line in f.read().split('\n') if line != ''] 
    
    for n in lst:
        if (2020-n) in lst: 
            print(f'answer to first puzzle of day {day} is: {n * (2020-n)}')
            break
    
    to_break = False
    for i, n in enumerate(lst):
        for j, m in enumerate(lst[i+1:]):
            if (2020-m-n) in lst: 
                print(f'answer to second puzzle of day {day} is: {n * m * (2020-m-n)}')
                to_break = True
                break
        
        if to_break: break
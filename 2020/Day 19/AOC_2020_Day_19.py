import os, sys, re

file_name = 'input_day_19.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    rules = [line.replace('"','').split(': ') for line in f.read().split('\n\n')[0].split('\n')]
    rules = {rule[0]:[i for i in re.split(r' |', rule[1]) if i != ''] for rule in rules}
    print(rules)        
    print(f.read().split('\n\n'))
    msgs = [line for line in f.read().split('\n\n')[1].split('\n')] 


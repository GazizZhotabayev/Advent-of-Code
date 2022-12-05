import os, sys

file_name = 'input_day_3.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    #parse the .txt into a list of integers
    lst = [line for line in f.read().split('\n')] 

convert = lambda x: ord(x) - 96 if x.islower() else convert(x.lower()) + 26

lst1 = [[line[:len(line)//2], line[len(line)//2:]] for line in lst]
lst1 = [set(sub[0]).intersection(set(sub[1])) for sub in lst1]
lst1 = [convert(list(sub)[0]) for sub in lst1]
ans1 = sum(lst1)
print(f'answer to first puzzle of day {day} is: {ans1}')

lst2 = [lst[i:i+3] for i in range(0, len(lst), 3)]
lst2 = [set.intersection(*[set(sub) for sub in group]) for group in lst2]
lst2 = [convert(list(sub)[0]) for sub in lst2]
ans2 = sum(lst2)
print(f'answer to second puzzle of day {day} is: {ans2}')
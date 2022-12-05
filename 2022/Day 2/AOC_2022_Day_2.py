import os, sys

file_name = 'input_day_2.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    #parse the .txt into a list of integers
    lst = [line.split() for line in f.read().split('\n')] 

convert = lambda x: int(x.translate(str.maketrans('ABCXYZ', '123123')))
lst = [[convert(hand) for hand in play] for play in lst]
def score(x, y):
    if x == y: return 3
    if x == 1 and y == 2: return 6
    if x == 2 and y == 3: return 6
    if x == 3 and y == 1: return 6
    return 0

lst1 = [score(hand[0], hand[1]) + hand[1] for hand in lst]
ans1 = sum(lst1)
print(f'answer to first puzzle of day {day} is: {ans1}')

def choice(x, y):
    if y == 2: return x
    if y == 1: 
        if x == 1: return 3
        if x == 2: return 1
        if x == 3: return 2
    if y == 3:
        if x == 1: return 2
        if x == 2: return 3
        if x == 3: return 1

lst2 = [score(hand[0], choice(hand[0], hand[1])) + choice(hand[0], hand[1]) for hand in lst]
ans2 = sum(lst2)
print(f'answer to second puzzle of day {day} is: {ans2}')
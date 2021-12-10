import os, sys
from itertools import permutations

file_name = 'input_day_21.txt'
#file_name = 'test_21.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = f.read().split('\n')
    
    FOOD, ALLERGENS = dict(), dict()
    def parse_line(line):
        food, allergens = line.split(' (contains ')
        food = food.split()
        allergens = set(allergens.strip(')').split(', '))
        for f in food:
            if f in FOOD:
                FOOD[f] += [set(allergens)]
            else:
                FOOD[f] = [set(allergens)]
        for a in allergens:
            if a in ALLERGENS:
                ALLERGENS[a] += [set(food)]
            else:
                ALLERGENS[a] = [set(food)]
    
    for line in lst:
        parse_line(line)

    print(len(FOOD), len(ALLERGENS))
import os, sys

file_name = 'input_day_21.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = f.read().split('\n')
    
    ALLERGENS = dict()
    def parse_line(line):
        food, allergies = line.split(' (contains ')
        food = food.split()
        allergies = set(allergies.strip(')').split(', '))
        for f in food:
            if f in ALLERGENS:
                ALLERGENS[f].union(set(allergies))
            else:
                ALLERGENS[f] = set(allergies)
    
    for line in lst:
        parse_line(line)

    print(ALLERGENS)
        
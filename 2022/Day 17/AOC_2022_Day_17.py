import os, sys
from copy import deepcopy
from itertools import cycle

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    wind = cycle(list(f.read()))

def generate_rock(i):
    if i % 5 == 0:
        rock = [list('..@@@@.')]
    elif i % 5 == 1:
        rock = [list(line) for line in '...@... ..@@@.. ...@...'.split()]
    elif i % 5 == 2:
        rock = [list(line) for line in '....@.. ....@.. ..@@@..'.split()]
    elif i % 5 == 3:
        rock = [list(line) for line in '..@.... ..@.... ..@.... ..@....'.split()]
    else:
        rock = [list(line) for line in '..@@... ..@@...'.split()]
    return rock

def push(grid, direction):
    original = deepcopy(grid)
    if direction == '>':
        for x, line in enumerate(grid):
            if '@' in line:
                i = line.index('@')
                j = len(line) - 1 - line[::-1].index('@')
                if j+1 >= len(line) or line[j+1] == '#':
                    return original
                else:
                    line[i] = '.'
                    line[j+1] = '@'
                    grid[x] = line  
    if direction == '<':
        for x, line in enumerate(grid):
            if '@' in line:
                i = line.index('@')
                j = len(line) - 1 - line[::-1].index('@')
                if i-1 < 0 or line[i-1] == '#':
                    return original
                else:
                    line[i-1] = '@'
                    line[j] = '.'
                    grid[x] = line  
    return grid

def fall(grid):
    original = deepcopy(grid)
    early_stop = False
    for i, line in enumerate(grid[::-1]):
        i = len(grid) - 1 - i
        if '@' in line:
            for j, c in enumerate(line):
                if c == '@':
                    if grid[i+1][j] in '#_':
                        grid[i][j] = '#'
                        return True, original
                    else:
                        grid[i+1][j] = '@'
                        grid[i][j] = '.'
    return False, grid

def pprint(list_of_lists):
    print('\n'.join(''.join(line) for line in list_of_lists))

grid = [['_' for i in range(7)]]
for i in range(3):
    grid.insert(0, ['.' for i in range(7)])

repetition = 0
for i in range(2022):
    rock = generate_rock(i)

    if i % 50 == 0: print(i)

    if i % 5 == 0:
        if repetition == 0:
            try:
                repetition = len(grid) - grid.index(list('#######'))
            except:
                pass
    
    while grid[2] != ['.' for i in range(7)]:
        grid.insert(0, ['.' for i in range(7)])

    grid = rock + grid

    while True:
        direction = next(wind)
        grid = push(grid, direction)
        stop, grid = fall(grid)
        if stop == True:
            grid = [['#' if x == '@' else x for x in line] for line in grid]
            break

    while len(grid) > 3 and ''.join(grid[0]) == '.' * 7:
        grid.pop(0)

ans1 = len(grid)-1
print(f'answer to first puzzle is: {ans1}')    

ans2 = 0
print(f'answer to first puzzle is: {ans2}')
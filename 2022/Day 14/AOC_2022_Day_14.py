import os, sys
from copy import deepcopy

file_name = 'input.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    instructions = f.read().split('\n')

m, n = 0, 0
for line in instructions:
    for pair in line.split(' -> '):
        x, y = [int(i) for i in pair.split(',')]
        if x > m: m = x+1
        if y > n: n = y+1

def parse(grid, line):
    line = [x.split(',') for x in line.split(' -> ')]
    line = [(int(x[0]), int(x[1])) for x in line]
    for p1, p2 in zip(line, line[1:]):
        y1, x1 = p1
        y2, x2 = p2
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2)+1):
                grid[x1][j] = '#'
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                grid[i][y1] = '#'
    return grid

GRID = [['.' for j in range(m+2)] for i in range(n+2)]
for line in instructions:
    GRID = parse(GRID, line)

count_sand = lambda grid: ''.join(''.join(line) for line in grid).count('o')

def simulate(grid):
    cnt = 0
    while True:
        x, y = 0, 500
        while True:
            if grid[x+1][y] == '.':
                x += 1
            else:
                if grid[x+1][y-1] == '.':
                    x += 1
                    y -= 1
                else:
                    if grid[x+1][y+1] == '.':
                        x += 1
                        y += 1
                    else:
                        grid[x][y] = 'o'
                        break
            if x > n:
                break
        
        c = count_sand(grid)
        if c > cnt:
            cnt = c
        else:
            break
    return cnt 

ans1 = simulate(deepcopy(GRID))
print(f'answer to first puzzle is: {ans1}')    

GRID = [['.' for j in range(m+200)] for i in range(n+2)]
for line in instructions:
    GRID = parse(GRID, line)
GRID[-1] = ['#' for i in range(len(GRID[0]))]

ans2 = simulate(deepcopy(GRID))
print(f'answer to first puzzle is: {ans2}')
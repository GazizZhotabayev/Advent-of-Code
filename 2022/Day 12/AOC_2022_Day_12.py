import os, sys
from numpy import inf
from copy import deepcopy

file_name = 'input.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    grid = [list(line) for line in f.read().split('\n')]

def shortest_path(GRID, start_node, direction):
    
    x, y = start_node
    DISTANCES = [[inf for j in range(len(GRID[0]))] for i in range(len(GRID))]
    DISTANCES[x][y] = 0
    UNVISITED = set([(i, j) for i in range(len(GRID)) for j in range(len(GRID[0]))])
    
    while True:

        candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        candidates = [(i, j) for i, j in candidates if 0 <= i < len(GRID) and 0 <= j < len(GRID[0])]
        if direction == 'up':
            candidates = [(i, j) for i, j in candidates if ord(GRID[i][j]) <= ord(GRID[x][y]) + 1]
        else:
            candidates = [(i, j) for i, j in candidates if ord(GRID[i][j]) >= ord(GRID[x][y]) - 1]
        candidates = [(i, j) for i, j in candidates if (i, j) in UNVISITED]

        for i, j in candidates:
            d = 1 + DISTANCES[x][y]
            if d < DISTANCES[i][j]:
                DISTANCES[i][j] = d
            
        UNVISITED.remove((x, y))
        try:
            x, y = min(UNVISITED, key = lambda node: DISTANCES[node[0]][node[1]])
        except:
            break 
            
    return DISTANCES

X = next(i for i, row in enumerate(grid) if 'E' in row)
Y = grid[X].index('E')
grid[X][Y] = 'z'

x = next(i for i, row in enumerate(grid) if 'S' in row)
y = grid[x].index('S')
grid[x][y] = 'a'

d1 = shortest_path(deepcopy(grid),(x, y), 'up')
ans1 = d1[X][Y]
print(f'answer to first puzzle is: {ans1}')

d2 = shortest_path(deepcopy(grid),(X, Y), 'down')
candidate_end_nodes = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'a']
ans2 = min([d2[i][j] for (i, j) in candidate_end_nodes])
print(f'answer to first puzzle is: {ans2}')
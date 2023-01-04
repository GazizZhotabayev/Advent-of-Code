import os, sys
from copy import deepcopy

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    GRID = [list(line) for line in f.read().split('\n')]
    BLIZZARDS = [(GRID[i][j], (i, j)) for i in range(len(GRID)) for j in range(len(GRID)) if GRID[i][j] not in '#.']
    M, N = len(GRID), len(GRID[0])

sys.setrecursionlimit(10**6)

def update_blizzards(m, n, blizzards):
    ans = set()
    for blizzard in list(blizzards):
        direction, position = blizzard
        x, y = position
        if direction == '>':
            if x < m-2:
                x += 1
            else:
                x = 1
        elif direction == '<':
            if x > 1:
                x -= 1
            else:
                x = m-2
        elif direction == 'v':
            if y < n-2:
                y += 1
            else:
                y = 1
        elif direction == '^':
            if y > 1:
                y -= 1
            else:
                y = n-2
        else:
            pass
        ans.add((direction, (x, y)))

    return ans

def possible_steps(m, n, blizzards, position):
    x, y = position
    options = [(x,y), (x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    blizzard_positions = [b[1] for b in blizzards]
    options = set([t for t in options if 1<=t[0]<m-1 and 1<=t[1]<n-1 and t not in blizzard_positions])
    return options

def count_to_exit(m, n, blizzards, position, cnt = 0):
    blizzards = update_blizzards(m, n, blizzards)
    options = possible_steps(m, n, blizzards, position)
    print(cnt)
    if (m-1, n-1) in options:
        return cnt+1
    else:
        for position in options:
            return count_to_exit(m, n, blizzards, position, cnt+1)

grid = deepcopy(GRID)
blizzards = deepcopy(BLIZZARDS)

ans1 = count_to_exit(M, N, BLIZZARDS, (0, 1))
print(f'answer to first puzzle is: {ans1}')    

ans2 = 0
print(f'answer to first puzzle is: {ans2}')
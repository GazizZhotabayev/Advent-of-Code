import os, sys
from copy import deepcopy
from collections import Counter

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    grid = [list(line) for line in f.read().split('\n')]
    elves = set([(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#'])

def new_position(elf, direction):
    x, y = elf
    if direction == 'north': return (x-1, y)
    if direction == 'south': return (x+1, y)
    if direction == 'west': return (x, y-1)
    if direction == 'east': return (x, y+1)
    return (x, y)

def first_half(ELVES, elf, directions):
    x, y = elf
    compass = {k: False for k in 'N NE NW S SE SW W E'.split()}
    if (x-1, y) in ELVES: compass['N'] = True
    if (x-1, y-1) in ELVES: compass['NW'] = True
    if (x-1, y+1) in ELVES: compass['NE'] = True 
    if (x+1, y) in ELVES: compass['S'] = True
    if (x+1, y-1) in ELVES: compass['SW'] = True
    if (x+1, y+1) in ELVES: compass['SE'] = True
    if (x, y-1) in ELVES: compass['W'] = True
    if (x, y+1) in ELVES: compass['E'] = True
    
    s = sum(compass.values())

    if s > 0:
        if not any(compass[k] for k in directions[0][1]):
            direction = directions[0][0]
        elif not any(compass[k] for k in directions[1][1]):
            direction = directions[1][0]
        elif not any(compass[k] for k in directions[2][1]):
            direction = directions[2][0]
        elif not any(compass[k] for k in directions[3][1]):
            direction = directions[3][0]
        else:
            direction = 'stay put'
    else:
        direction = 'stay put'

    return new_position(elf, direction)

def second_half(ELVES, directions):
    PROPOSALS = {elf: first_half(ELVES, elf, directions) for elf in list(ELVES)}
    
    C = Counter(PROPOSALS.values())
    ans = set()
    for k, v in PROPOSALS.items():
        if C[v] > 1:
            ans.add(k)
        else:
            ans.add(v)

    moved = ans != ELVES
    return ans, moved

directions = []
directions += [('north', 'N NE NW'.split())]
directions += [('south', 'S SE SW'.split())]
directions += [('west', 'W NW SW'.split())]
directions += [('east', 'E NE SE'.split())]

cnt = 0
while True:
    cnt += 1
    elves, moved = second_half(elves, directions)
    directions = directions[1:] + directions[:1]
    if cnt == 10:
        x1, x2 = min([t[0] for t in elves]), max([t[0] for t in elves])
        y1, y2 = min([t[1] for t in elves]), max([t[1] for t in elves])
        ans1 = abs(x2-x1+1) * abs(y2-y1+1) - len(elves)
    if moved == False:
        break

print(f'answer to first puzzle is: {ans1}')    

ans2 = cnt
print(f'answer to first puzzle is: {ans2}')
import os, sys
from operator import mul
from functools import reduce # python3 compatibility

file_name = 'input.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    grid = [[int(i) for i in line] for line in f.read().split('\n')]

m, n = len(grid), len(grid[0])

visible = set()

for i in range(m):
    for j in range(n):
        x = grid[i][j]
        #look up
        if all(x > grid[k][j] for k in range(0, i)):
            visible.add((i, j))
        #look down
        elif all(x > grid[k][j] for k in range(i+1, m)):
            visible.add((i, j))
        #look left
        elif all(x > grid[i][l] for l in range(0, j)):
            visible.add((i, j))
        #look right
        elif all(x > grid[i][l] for l in range(j+1, n)):
            visible.add((i, j))
        else:
            pass

scores = []
for i in range(m):
    for j in range(n):
        x = grid[i][j]
        up, down, left, right = 0, 0, 0, 0
        #look up
        for k in range(i-1, -1, -1):
            if x > grid[k][j]:
                up += 1
            else:
                up += 1
                break
        #look down
        for k in range(i+1, m):
            if x > grid[k][j]:
                down += 1
            else:
                down += 1
                break
        #look left
        for l in range(j-1, -1, -1):
            if x > grid[i][l]:
                left += 1
            else:
                left += 1
                break
        #look right
        for l in range(j+1, n):
            if x > grid[i][l]:
                right += 1
            else:
                right += 1
                break
        score = up * down * left * right
        scores.append(score)

ans1 = len(visible)
print(f'answer to first puzzle is: {ans1}')

ans2 = max(scores)
print(f'answer to second puzzle is: {ans2}')
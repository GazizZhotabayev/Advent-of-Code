import os, sys
import numpy as np

file_name = 'input_day_17.txt'
#file_name = 'test_17.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line for line in f.read().split('\n') if line != ''] 
    lst = [[1 if i == '#' else 0 for i in line] for line in lst]

    swap = lambda x: 1 if x == 0 else 0

    def active_neighbours(cube, x, y, z):
        cnt = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    try:
                        if i == j == k == 0: continue
                        if x+i < 0 or y+j < 0 or z+k < 0: continue
                        if cube[x+i][y+j][z+k] == 1: cnt += 1
                    except: pass
        return cnt

    def switch(cube, x, y, z):
        cnt = active_neighbours(cube, x, y, z)
        if cube[x][y][z] == 1 and not (cnt in (2,3)): return True
        if cube[x][y][z] == 0 and cnt == 3: return True
        return False

    l = 6
    arr = lst[:]
    arr = [[0] * l + sub + [0] * l for sub in arr]
    arr = [[0] * len(arr[0])] * l + arr + [[0] *  len(arr[0])] * l

    n = len(arr)
    sheet = [[0] * n] * n
    arr = [sheet] * ((n-1)//2) + [arr] + [sheet] * ((n-1)//2)
    m = len(arr)

    for cycle in range(6):
        arr = [[[swap(arr[i][j][k]) if switch(arr, i, j, k) else arr[i][j][k] for k in range(n)] for j in range(n)] for i in range(m)]
    
    ans1 = sum(n for sub1 in arr for sub2 in sub1 for n in sub2)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    def active_neighbours(cube, x, y, z, w):
        cnt = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        try:
                            if i == j == k == l == 0: continue
                            if x+i < 0 or y+j < 0 or z+k < 0 or w+l < 0: continue
                            if cube[x+i][y+j][z+k][w+l] == 1: cnt += 1
                        except: pass
        return cnt

    def switch(cube, x, y, z, w):
        cnt = active_neighbours(cube, x, y, z, w)
        if cube[x][y][z][w] == 1 and not (cnt in (2,3)): return True
        if cube[x][y][z][w] == 0 and cnt == 3: return True
        return False

    l = 6
    arr = lst[:]
    arr = [[0] * l + sub + [0] * l for sub in arr]
    arr = [[0] * len(arr[0])] * l + arr + [[0] *  len(arr[0])] * l

    n = len(arr)
    sheet = [[0] * n] * n
    arr = [sheet] * ((n-1)//2) + [arr] + [sheet] * ((n-1)//2)
    m = len(arr)
    sheet3d = [[[0] * n] * n] * m
    arr = [sheet3d] * (m//2) + [arr] + [sheet3d] * (m//2)

    for cycle in range(6):
        arr = [[[[swap(arr[i][j][k][l]) if switch(arr, i, j, k, l) else arr[i][j][k][l] for l in range(n)] for k in range(n)] for j in range(m)] for i in range(m)]
    
    ans2 = sum(n for sub1 in arr for sub2 in sub1 for sub3 in sub2 for n in sub3)
    print(f'answer to second puzzle of day {day} is: {ans2}')
import os, sys

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    cubes = [tuple(int(x) for x in cube.split(',')) for cube in f.read().split('\n')]

#minx, maxx = min(cube[0] for cube in cubes), max(cube[0] for cube in cubes)
#miny, maxy = min(cube[1] for cube in cubes), max(cube[1] for cube in cubes)
#minz, maxz = min(cube[2] for cube in cubes), max(cube[2] for cube in cubes)
#print(minx,maxx,miny,maxy,minz,maxz)

CUBES = set(cubes)
COUNTS = []
for cube in cubes:
    cnt = 6
    x, y, z = cube
    if (x-1, y, z) in CUBES: cnt -= 1
    if (x+1, y, z) in CUBES: cnt -= 1
    if (x, y-1, z) in CUBES: cnt -= 1
    if (x, y+1, z) in CUBES: cnt -= 1
    if (x, y, z-1) in CUBES: cnt -= 1
    if (x, y, z+1) in CUBES: cnt -= 1
    COUNTS.append(cnt)

ans1 = sum(COUNTS)
print(f'answer to first puzzle is: {ans1}')    

ans2 = 0
print(f'answer to first puzzle is: {ans2}')
import os, sys

file_name = 'input_day_11.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    GRID = [[(int(octopus), False) for octopus in line] for line in f.read().split('\n')]
    
    #the tuple will hold the octopus energy level + whether it has already contributed to adjacent octopi 

    def cnt_adjacent(grid, x, y):
        cnt = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x+i >= 0 and x+i < len(grid) and y+j >=0 and y+j < len(grid[0]) and len(grid[0]) and not (i==j==0) and grid[x+i][y+j][0] == 0 and not(grid[x+i][y+j][1]):
                    cnt += 1
        return cnt

    def step(grid):
        grid = [[(octopus[0] + 1, octopus[1]) for octopus in line] for line in grid]
        FLASHES = 0
        while True:
            flashes = sum(1 for line in grid for octopus in line if octopus[0] > 9)
            if flashes == 0: break
            FLASHES += flashes
            grid = [[octopus if octopus[0] < 10 else (0, octopus[1]) for octopus in line] for line in grid]
            grid = [[(0, True) if octopus[0] == 0 else (octopus[0] + cnt_adjacent(grid, i, j), octopus[1]) for j, octopus in enumerate(line)] for i, line in enumerate(grid)]

        return grid, FLASHES

    def pprint(grid): 
        for line in grid: print(line)

    ans1 = 0
    for i in range(1, 101):
        GRID, x = step(GRID)
        GRID = [[(octopus[0], False) for octopus in line] for line in GRID]
        ans1 += x
        print(i)

    print(f'answer to first puzzle of day {day} is: {ans1}')

    while True:
        GRID, x = step(GRID)
        GRID = [[(octopus[0], False) for octopus in line] for line in GRID]
        i += 1
        if sum(sum(octopus[0] for octopus in line) for line in GRID) == 0: 
            break

    ans2 = i
    print(f'answer to second puzzle of day {day} is: {ans2}')
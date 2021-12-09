import os, sys

file_name = 'input_day_9.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    grid = [[int(i) for i in line] for line in f.read().split('\n')]
    
    def is_lowest(grid, x, y):
        max_cnt, cnt, point = 4, 0, grid[x][y]
        if x == 0: max_cnt -= 1
        if y == 0: max_cnt -= 1
        if x == len(grid) - 1: max_cnt -=1
        if y == len(grid[0]) - 1: max_cnt -= 1 
        if x+1 < len(grid) and grid[x+1][y] > point: cnt += 1
        if x-1 >= 0 and grid[x-1][y] > point: cnt += 1
        if y+1 < len(grid[0]) and grid[x][y+1] > point: cnt += 1
        if y-1 >= 0 and grid[x][y-1] > point: cnt += 1
        return True if cnt == max_cnt else 0

    def risk(grid, x, y):
        return grid[x][y] + 1 if is_lowest(grid, x, y) else 0 

    ans1 = sum(risk(grid, x, y) for x in range(len(grid)) for y in range(len(grid[0])))
    print(f'answer to first puzzle of day {day} is: {ans1}')

    def find_basin(grid, x, y, basin = []):
        point = grid[x][y]
        if point == 9: return []
        if (x,y) not in basin: basin.extend([(x, y)])
        if x+1 < len(grid) and (x+1, y) not in basin: basin.extend(find_basin(grid, x+1, y, basin))
        if x-1 >= 0 and (x-1, y) not in basin: basin.extend(find_basin(grid, x-1, y, basin))
        if y+1 < len(grid[0]) and (x, y+1) not in basin: basin.extend(find_basin(grid, x, y+1, basin))
        if y-1 >= 0 and (x, y-1) not in basin: basin.extend(find_basin(grid, x, y-1, basin))
        return list(set(basin))

    BASINS = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
           if (x, y) in [point for basin in BASINS for point in basin]: continue
           basin = find_basin(grid, x, y, [])
           if len(basin) > 0: BASINS.append(basin)
    
    BASINS = sorted(BASINS, key = len)
    ans2 = len(BASINS[-1]) * len(BASINS[-2]) * len(BASINS[-3])
    print(f'answer to second puzzle of day {day} is: {ans2}')
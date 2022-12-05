import os, sys

file_name = 'input_day_25.txt'
file_name = 'test_25.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    GRID = [list(line) for line in f.read().split('\n')]
    M, N = len(GRID), len(GRID[0])

    def step(grid):
        m, n = len(grid), len(grid[0])
        get_dwn = lambda i, j: grid[i+1][j] if i+1 < m else grid[0][j]
        get_up = lambda i, j: grid[i-1][j] if i-1 >= 0 else grid[m-1][j]
        get_fwd = lambda i, j: grid[i][j+1] if j+1 < n else grid[i][0]
        get_bck = lambda i, j: grid[i][j-1] if j-1 >= 0 else grid[i][n-1]
        
        #move east
        grid = [['.' if (grid[i][j] == '>' and get_fwd(i,j) == '.') else '>' if (grid[i][j] == '.' and get_bck(i,j) == '>')  else grid[i][j] for j in range(n)] for i in range(m)] 
        #move south
        grid = [['.' if (grid[i][j] == 'v' and get_dwn(i,j) == '.') else 'v' if (grid[i][j] == '.' and get_up(i,j) == 'v')  else grid[i][j] for j in range(n)] for i in range(m)] 
        
        return grid

    steps = 0
    while True:
        OLD = [x[:] for x in GRID]
        GRID = step(GRID)
        steps += 1
        if OLD == GRID: break

    ans1 = steps
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = 0
    print(f'answer to second puzzle of day {day} is: {ans2}')

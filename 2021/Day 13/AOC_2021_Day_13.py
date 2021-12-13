import os, sys

file_name = 'input_day_13.txt'
#file_name = 'test_13.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    dots, instructions = f.read().split('\n\n')
    dots = [tuple([int(i) for i in line.split(',')]) for line in dots.split('\n')]
    instructions = instructions.split('\n')

    n, m = max([x for x, y in dots]), max([y for x, y in dots])

    GRID = [['.' for j in range(n+1)] for i in range(m+1)]
    for j, i in dots: GRID[i][j] = '#'

    def fold(grid, instruction):
        axis, v = instruction.split()[-1].split('=')
        v = int(v)
        m, n = len(grid), len(grid[0])

        if axis == 'x':
            left, right = [[grid[i][j] for j in range(v)] for i in range(m)], [[grid[i][j] for j in range(v+1, n)] for i in range(m)]
            
            if len(left[0]) >= len(right[0]):
                gap = [[left[i][j] for j in range(v+1-(n-v))] for i in range(m)]
                left = [[left[i][j] for j in range(v+1-(n-v), v)] for i in range(m)]
                right = [[right[i][j] for j in range(len(right[0])-1, -1, -1)] for i in range(m)]
            else:
                gap = [[right[i][j] for j in range(len(right[0])-1, v-1, -1)] for i in range(m)]
                right = [[right[i][j] for j in range(v-1, -1, -1)] for i in range(m)]
            
            #correct outcome should then be gap + (overlap of left + right)
            grid = [gap[i] + ['#' if left[i][j] == '#' or right[i][j] == '#' else '.' for j in range(v)] for i in range(m)]

        if axis == 'y':
            top, bottom = [[grid[i][j] for j in range(n)] for i in range(v)], [[grid[i][j] for j in range(n)] for i in range(v+1, m)]

            if len(top) >= len(bottom):
                gap = [[top[i][j] for j in range(n)] for i in range(v+1-(m-v))]
                top = [[top[i][j] for j in range(n)] for i in range(v+1-(m-v), v)]
                bottom = [[bottom[i][j] for j in range(n)] for i in range(len(bottom)-1, -1, -1)]
            else:
                gap = [[bottom[i][j] for j in range(n)] for i in range(len(bottom)-1, v-1, -1)]
                bottom = [[bottom[i][j] for j in range(n)] for i in range(v-1, -1, -1)]
        
            #correct outcome should then be gap + (overlap of top + bottom)
            grid = gap + [['#' if top[i][j] == '#' or bottom[i][j] == '#' else '.' for j in range(n)] for i in range(v)]

        return grid

    count_dots = lambda grid: sum(1 for row in grid for point in row if point == '#')

    ans1 = count_dots(fold(GRID, instructions[0]))
    print(f'answer to first puzzle of day {day} is: {ans1}')

    for instruction in instructions:
        GRID = fold(GRID, instruction)

    print(f'answer to second puzzle of day {day} is:')
    for line in GRID: print(line)

import os, sys, re

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    GRID, instructions = f.read().split('\n\n')

maxx = max(len(line) for line in GRID.split('\n'))
GRID = [list(line.ljust(maxx)) for line in GRID.split('\n')]
instructions = re.split(r'([A-Z])', instructions)

def turn(letter, current_direction):
    order = 'up right down left'.split()
    if letter == 'R':
        return order[(order.index(current_direction)+1)%4]
    if letter == 'L':
        return order[(order.index(current_direction)-1)%4]

def move(grid, instruction, position, direction):
    x, y = position
    
    if instruction.isnumeric():
        n = int(instruction)
        for _ in range(n):
            if direction == 'right':
                if len(grid[x]) < y+2 or grid[x][y+1] == ' ':
                    j = next(_ for _, c in enumerate(grid[x]) if c in '#.')
                    if grid[x][j] == '#': 
                        break
                    y = j
                elif grid[x][y+1] == '#': 
                    break
                else:
                    y += 1
            elif direction == 'left':
                if y == 0 or grid[x][y-1] == ' ':
                    j = len(grid[x]) - 1 - next(_ for _, c in enumerate(grid[x][::-1]) if c in '#.')
                    if grid[x][j] == '#': 
                        break
                    y = j
                elif grid[x][y-1] == '#': 
                    break
                else:
                    y -= 1
            elif direction == 'down':
                if len(grid) < x+2 or grid[x+1][y] == ' ':
                    i = next(_ for _, line in enumerate(grid) if line[y] in '#.')
                    if grid[i][y] == '#': 
                        break
                    x = i
                elif grid[x+1][y] == '#': 
                    break
                else:
                    x += 1
            elif direction == 'up':
                if x == 0 or grid[x-1][y] == ' ':
                    i = len(grid) - 1 - next(_ for _, line in enumerate(grid[::-1]) if line[y] in '#.')
                    if grid[i][y] == '#': 
                        break
                    x = i
                elif grid[x-1][y] == '#': 
                    break
                else:
                    x -= 1
            else:
                pass
    else:
        direction = turn(instruction, direction)

    return (x, y), direction

position, direction = (0, GRID[0].index('.')), 'right'
for instruction in instructions:
    position, direction = move(GRID, instruction, position, direction)

x, y = position
facing = 'right down left up'.split().index(direction)
ans1 = 1000 * (x+1) + 4 * (y+1) + facing
print(f'answer to first puzzle is: {ans1}')    

ans2 = 0
print(f'answer to first puzzle is: {ans2}')
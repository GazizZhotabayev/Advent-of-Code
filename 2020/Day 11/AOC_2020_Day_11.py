import os, sys

file_name = 'input_day_11.txt'
#file_name = 'test_11.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    seats = [line for line in f.read().split('\n')] 

    def count_seats(grid, x, y):
        m, n, cnt = len(grid), len(grid[0]), 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if all((x+i>=0, x+i<m, y+j>=0, y+j<n, not(i==j==0))):
                    if grid[x+i][y+j]=="#": 
                        cnt += 1
        return cnt

    def update_seat(grid, x, y):
        cnt = count_seats(grid, x, y)
        if grid[x][y] == 'L' and cnt == 0:
            c = '#'
        elif grid[x][y] == '#' and cnt >= 4:
            c = 'L'
        else:
            c = grid[x][y]
        return c

    seats1 = [[seats[i][j] for j in range(len(seats[0]))] for i in range(len(seats))]
    while True:
        new = [[update_seat(seats1, i, j) for j in range(len(seats[0]))] for i in range(len(seats))]
        if new == seats1:
            break
        else:
            seats1 = [[new[i][j] for j in range(len(seats[0]))] for i in range(len(seats))]
    
    ans1 = sum(1 for i in range(len(seats)) for j in range(len(seats[0])) if seats1[i][j] == '#')
    print(f'answer to first puzzle of day {day} is: {ans1}')

    def count_seats_2(grid, x, y):
        m, n, cnt = len(grid), len(grid[0]), 0
        for i in range(x-1, -1,-1): #up
            if grid[i][y] == '#': 
                cnt += 1
                break
            if grid[i][y] == "L": break
        for i in range(x+1, m): #down
            if grid[i][y] == '#': 
                cnt += 1
                break
            if grid[i][y] == "L": break
        for j in range(y-1, -1, -1): #left
            if grid[x][j] == '#': 
                cnt += 1
                break
            if grid[x][j] == "L": break
        for j in range(y+1, n): #right
            if grid[x][j] == '#': 
                cnt += 1
                break
            if grid[x][j] == "L": break
        
        i = 1
        while True: #up-left
            if x-i < 0 or y-i < 0: break
            if grid[x-i][y-i] == '#': 
                cnt += 1
                break
            if grid[x-i][y-i] == "L": break
            i += 1

        i = 1
        while True: #up-right
            if x-i < 0 or y+i >= n: break
            if grid[x-i][y+i] == '#': 
                cnt += 1
                break
            if grid[x-i][y+i] == "L": break
            i += 1

        i = 1
        while True: #down-left
            if x+i >= m or y-i < 0: break
            if grid[x+i][y-i] == '#': 
                cnt += 1
                break
            if grid[x+i][y-i] == "L": break
            i += 1

        i = 1
        while True: #down-right
            if x+i >= m or y+i >= n: break
            if grid[x+i][y+i] == '#': 
                cnt += 1
                break
            if grid[x+i][y+i] == "L": break
            i += 1

        return cnt

    def update_seat_2(grid, x, y):
        cnt = count_seats_2(grid, x, y)
        if grid[x][y] == 'L' and cnt == 0:
            c = '#'
        elif grid[x][y] == '#' and cnt >= 5:
            c = 'L'
        else:
            c = grid[x][y]
        return c

    seats2 = [[seats[i][j] for j in range(len(seats[0]))] for i in range(len(seats))]
    while True:
        new = [[update_seat_2(seats2, i, j) for j in range(len(seats[0]))] for i in range(len(seats))]
        if new == seats2:
            break
        else:
            seats2 = [[new[i][j] for j in range(len(seats[0]))] for i in range(len(seats))]
    
    ans2 = sum(1 for i in range(len(seats)) for j in range(len(seats[0])) if seats2[i][j] == '#')
    print(f'answer to second puzzle of day {day} is: {ans2}')
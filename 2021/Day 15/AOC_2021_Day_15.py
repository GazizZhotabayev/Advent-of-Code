import os, sys

file_name = 'input_day_15.txt'
#file_name = 'test_15.txt'
day = file_name.split('.')[0].split('_')[-1]

#https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
with open(os.path.join(sys.path[0], file_name)) as f:
    block = [[int(i) for i in line] for line in f.read().split('\n')]
    
    def solve(risk):
        m, n = len(risk), len(risk[0])
        
        RISK = [[10**10 for j in range(n)] for i in range(m)]
        RISK[0][0] = 0
        VISITED = set()
        UNVISITED = set([(x, y) for x in range(m) for y in range(n)])
        coords = ((1,0), (0,1), (-1,0), (0,-1))
        
        current = (0,0)
        while True:
            x, y = current
            UNVISITED.remove((x, y))
            print(len(VISITED))
            neighbours = [(x+i, y+j) for i, j in coords if 0 <= x+i < m and 0 <= y+j < n and (x+i, y+j) not in VISITED]

            for u, v in neighbours:
                d = RISK[x][y] + risk[u][v]
                if d < RISK[u][v]:
                    RISK[u][v] = d

            VISITED.add(current)
            if len(VISITED) < m * n:
                current = min(UNVISITED, key = lambda t: RISK[t[0]][t[1]])
            else:
                break
        
        return RISK[-1][-1]
    
    ans1 = solve(block)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    m, n = len(block[0]), len(block)
    BLOCK = [[0 for j in range(n * 5)] for i in range(m * 5)]
    for i in range(len(BLOCK)):
        for j in range(len(BLOCK[0])):
            k, l = i // m, j // n
            BLOCK[i][j] = block[i%m][j%n] + k + l if block[i%m][j%n] + k + l < 10 else block[i%m][j%n] + k + l - 9 
    
    ans2 = solve(BLOCK)
    print(f'answer to second puzzle of day {day} is: {ans2}')
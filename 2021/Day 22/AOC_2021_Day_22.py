import os, sys

file_name = 'input_day_22.txt'
#file_name = 'test_22.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:

    def parse(line):
        instruction, coords = line.split()
        x, y, z = coords.split(',')
        x = x.split('=')[1].split('..')
        y = y.split('=')[1].split('..')
        z = z.split('=')[1].split('..')
        return (instruction, (int(x[0]), int(y[0]), int(z[0])), (int(x[1]), int(y[1]), int(z[1])))

    INSTRUCTIONS = [parse(line) for line in f.read().split('\n')]

    def limit_line(line, limit):
        l1, l2 = limit * (-1), limit
        x1, y1, z1 = line[1]
        x2, y2, z2 = line[2]
        
        if x2<l1 or y2<l1 or z2<l1 or x1>l2 or y1>l2 or z1>l2: return "invalid point"
        
        x1, y1, z1 = max(l1, x1), max(l1, y1), max(l1, z1)
        x2, y2, z2 = min(l2, x2), min(l2, y2), min(l2, z2)
        return (line[0], (x1, y1, z1), (x2, y2, z2))

    #INSTRUCTIONS = [limit_line(line, 50) for line in INSTRUCTIONS if limit_line(line, 50) != "invalid point"]
    x_min = min([x1 for i, (x1, y1, z1), (x2, y2, z2) in INSTRUCTIONS])
    y_min = min([y1 for i, (x1, y1, z1), (x2, y2, z2) in INSTRUCTIONS])
    z_min = min([z1 for i, (x1, y1, z1), (x2, y2, z2) in INSTRUCTIONS])

    x_max = max([x2 for i, (x1, y1, z1), (x2, y2, z2) in INSTRUCTIONS])
    y_max = max([y2 for i, (x1, y1, z1), (x2, y2, z2) in INSTRUCTIONS])
    z_max = max([z2 for i, (x1, y1, z1), (x2, y2, z2) in INSTRUCTIONS])

    #go over each point in the total space and apply each instruction in turn if the point falls under them 
    x_min = y_min = z_min = -50
    x_max = y_max = z_max = 50
    cnt = 0
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            for k in range(z_min, z_max+1):
                state = 'off'
                for line in INSTRUCTIONS:
                    instruction = line[0]
                    x1, y1, z1 = line[1]
                    x2, y2, z2 = line[2]
                    if x1<=i<=x2 and y1<=j<=y2 and z1<=k<=z2:
                        state = instruction
                if state == 'on': cnt += 1
    
    ans1 = cnt
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = 0
    print(f'answer to second puzzle of day {day} is: {ans2}')

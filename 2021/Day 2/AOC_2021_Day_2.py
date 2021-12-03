import os, sys

file_name = 'input_day_2.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line.split() for line in f.read().split('\n') if line != '']
    depth = sum(int(j) if i == 'down' else -int(j) if i == 'up' else 0 for i, j in lst)
    horizontal = sum(int(j) for i, j in lst if i == 'forward')
    print(f'answer to first puzzle of day {day} is: {depth * horizontal}')

    aim, depth, horizontal = 0, 0, 0
    for i in lst:
        command, x = i[0], int(i[1])
        if command == 'down':
            aim += x
        elif command == 'up':
            aim -= x
        elif command == 'forward':
            horizontal += x
            depth += aim * x
        else:
            pass
        
    print(f'answer to second puzzle of day {day} is: {depth * horizontal}')
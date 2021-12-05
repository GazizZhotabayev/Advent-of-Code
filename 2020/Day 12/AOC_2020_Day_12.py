import os, sys

file_name = 'input_day_12.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line for line in f.read().split('\n')] 

    def move(action, direction, value, x, y):
        if action == 'F':
            return move(direction, direction, value, x, y)
        elif action == 'N':
            y -= value
        elif action == 'S':
            y += value
        elif action == 'W':
            x -= value
        elif action == 'E':
            x += value
        elif action == 'L':
            if value == 90:
                return move('F', {'N':'W', 'E':'N', 'S':'E', 'W':'S'}[direction], 0, x, y)
            if value == 180:
                return move('F', {'N':'S', 'E':'W', 'S':'N', 'W':'E'}[direction], 0, x, y)
            if value == 270:
                return move('F', {'N':'E', 'E':'S', 'S':'W', 'W':'N'}[direction], 0, x, y)
        elif action == 'R':
            if value == 90:
                return move('F', {'N':'E', 'E':'S', 'S':'W', 'W':'N'}[direction], 0, x, y)
            if value == 180:
                return move('F', {'N':'S', 'E':'W', 'S':'N', 'W':'E'}[direction], 0, x, y)
            if value == 270:
                return move('F', {'N':'W', 'E':'N', 'S':'E', 'W':'S'}[direction], 0, x, y)
        else:
            pass

        return direction, x, y

    direction, x, y = 'E', 0, 0
    for line in lst:
        direction, x, y = move(line[0], direction, int(line[1:]), x, y)
        
    ans1 = abs(x) + abs(y)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    def move_2(action, value, x, y, waypoint):
        if action == 'F':
            x += waypoint[0] * value
            y += waypoint[1] * value
        elif action == 'N':
            waypoint[1] -= value
        elif action == 'S':
            waypoint[1] += value
        elif action == 'W':
            waypoint[0] -= value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'L':
            if value == 90:
                return x, y, [waypoint[1], waypoint[0]*(-1)]
            if value == 180:
                return x, y, [waypoint[0]*(-1), waypoint[1]*(-1)]
            if value == 270:
                return x, y, [waypoint[1]*(-1), waypoint[0]]
        elif action == 'R':
            if value == 90:
                return x, y, [waypoint[1]*(-1), waypoint[0]]
            if value == 180:
                return x, y, [waypoint[0]*(-1), waypoint[1]*(-1)]
            if value == 270:
                return x, y, [waypoint[1], waypoint[0]*(-1)]
        else:
            pass

        return x, y, waypoint

    x, y, waypoint = 0, 0, [10, -1]
    for line in lst:
        x, y, waypoint = move_2(line[0], int(line[1:]), x, y, waypoint)
        
    ans2 = abs(x) + abs(y)
    print(f'answer to second puzzle of day {day} is: {ans2}')
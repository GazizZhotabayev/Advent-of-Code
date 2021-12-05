import os, sys
from collections import Counter

file_name = 'input_day_5.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lines = [line for line in f.read().split('\n')]

    def count_points(grid, diagonal = False):
        points = []
        for line in lines:
            p1, p2 = line.split(' -> ')
            x1, y1 = [int(i) for i in p1.split(',')]
            x2, y2 = [int(i) for i in p2.split(',')]
            if x1 == x2 and y1 == y2: points.append((x1, y1))
            elif x1 == x2:
                points += [(x1, i) for i in range(min(y1, y2), max(y1, y2)+1)]
            elif y1 == y2:
                points += [(i, y1) for i in range(min(x1, x2), max(x1, x2)+1)]
            elif diagonal and abs(x1-x2) == abs(y1-y2):
                step_x = -1 if x1 > x2 else 1
                step_y = -1 if y1 > y2 else 1
                if step_x == step_y:
                    points += [(min(x1, x2) + i, min(y1, y2) + i) for i in range(max(x1, x2) - min(x1, x2) + 1)]
                else:
                    points += [(min(x1, x2) + i, max(y1, y2) - i) for i in range(max(x1, x2) - min(x1, x2) + 1)]
            else:
                pass

        return Counter(points)
    
    ans1 = sum(1 for k, v in count_points(lines).items() if v > 1)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = sum(1 for k, v in count_points(lines, diagonal = True).items() if v > 1)
    print(f'answer to second puzzle of day {day} is: {ans2}')
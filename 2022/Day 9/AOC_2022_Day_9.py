import os, sys

file_name = 'input.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    instructions = f.read().split('\n')

def move_head(direction, head):
    x, y = head
    if direction == 'L':
        x += -1
    if direction == 'R':
        x += 1
    if direction == 'U':
        y += -1
    if direction == 'D':
        y += 1
    return (x, y)

def move_tail(head, tail):
    x, y = head
    i, j = tail
    if abs(x-i) > 1 and y == j:
        if x > i: i += 1
        if x < i: i += -1
    elif abs(y-j) > 1 and x == i:
        if y > j: j += 1
        if y < j: j += -1
    elif (abs(x-i) > 1 and abs(y-j) >= 1) or (abs(y-j) > 1 and abs(x-i) >= 1):
        if x > i and y > j:
            i += 1
            j += 1
        elif x > i and y < j:
            i += 1
            j += -1
        elif x < i and y > j:
            i += -1
            j += 1
        elif x < i and y < j:
            i += -1
            j += -1
        else:
            pass
    else:
        pass

    return (i, j)

origin = (0, 0)
HEAD = [origin]
TAILS = {key:[origin] for key in range(9)}
for instruction in instructions:
    direction, cnt = instruction.split()
    cnt = int(cnt)
    while cnt > 0:
        head = move_head(direction, HEAD[-1])
        HEAD.append(head)
        for i in range(9):
            head = HEAD[-1] if i == 0 else TAILS[i-1][-1]
            tail = move_tail(head, TAILS[i][-1])
            TAILS[i].append(tail)
        cnt += -1

ans1 = len(set(TAILS[0]))
print(f'answer to first puzzle is: {ans1}')

ans2 = len(set(TAILS[8]))
print(f'answer to second puzzle is: {ans2}')

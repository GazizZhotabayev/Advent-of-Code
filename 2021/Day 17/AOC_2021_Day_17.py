day = 17
x_target1, x_target2, y_target1, y_target2 = 25, 67, -260, -200 
#x_target1, x_target2, y_target1, y_target2 = 20, 30, -10, -5

def evaluate(v_x, v_y):
    x, y, step, max_y = 0, 0, 0, 0

    landed = False
    while True:
        x += v_x
        y += v_y
        v_x = v_x + 1 if v_x < 0 else v_x - 1 if v_x > 0 else 0
        v_y -= 1
        step += 1

        if y > max_y: max_y = y
        if x_target1 <= x <= x_target2 and y_target1 <= y <= y_target2: landed = True
        if x > x_target2 or y < y_target1 or x == y == 0: break

    return landed, max_y

MAX_Y = set()
INITIAL_VELOCITIES = set()
for v_x in range(70):
    for v_y in range(-260, 1000):
        landed, max_y = evaluate(v_x, v_y)
        if landed: 
            MAX_Y.add(max_y)
            INITIAL_VELOCITIES.add((v_x, v_y))

ans1 = max(MAX_Y)
print(f'answer to first puzzle of day {day} is: {ans1}')

ans2 = len(INITIAL_VELOCITIES)
print(f'answer to second puzzle of day {day} is: {ans2}')
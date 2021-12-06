day = 25

card_public_key = 9232416
door_public_key = 14144084
subject_number = 7

KEYS = [0, subject_number % 20201227]
for i in range(10 ** 8): KEYS += [(KEYS[-1] * subject_number) % 20201227]

card_loop_size, door_loop_size = KEYS.index(card_public_key), KEYS.index(door_public_key)

def transform(subject_number, loop_size):
    x = 1
    for i in range(loop_size):
        x *= subject_number
        x = x % 20201227
    return x

ans1 = transform(card_public_key, door_loop_size)
print(f'answer to first puzzle of day {day} is: {ans1}')

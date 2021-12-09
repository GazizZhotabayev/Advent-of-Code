import os, sys

day = 23

label = [int(i) for i in '326519478']
#label = [int(i) for i in '389125467']

def move(CUPS, current_cup_index):
    current_cup = CUPS[current_cup_index]
    picked_cups_indices = [i % len(CUPS) for i in range(current_cup_index+1, current_cup_index+4)]
    
    PICKED_CUPS = [CUPS[i] for i in picked_cups_indices]
    CUPS = [CUPS[i] for i, c in enumerate(CUPS) if i not in picked_cups_indices]

    try:
        destination_cup = max([cup for cup in CUPS if cup < current_cup])
    except:
        destination_cup = max([cup for cup in CUPS if cup != current_cup])

    destination_cup_index = CUPS.index(destination_cup)
    print(current_cup, PICKED_CUPS, destination_cup)
    CUPS = CUPS[:destination_cup_index+1] + PICKED_CUPS + CUPS[destination_cup_index+1:]
    return CUPS, (CUPS.index(current_cup)+1) % len(CUPS)

x = 0
for i in range(100):
    print(f'move: {i+1}, {label}')
    label, x = move(label, x)

i = label.index(1)
ans1 = ''.join([str(c) for c in label[i+1:] + label[:i]])
print(f'answer to first puzzle of day {day} is: {ans1}')
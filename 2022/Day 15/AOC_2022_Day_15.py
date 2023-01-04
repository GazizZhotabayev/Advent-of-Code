import os, sys

file_name = 'input.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    instructions = f.read().split('\n')

SENSORS, BEACONS = dict(), set()
for instruction in instructions:
    sensor, beacon = [x.split(',') for x in instruction.split(':')]
    sensor = [int(''.join(i for i in coord if i.isnumeric())) for coord in sensor]
    beacon = [int(''.join(i for i in coord if i.isnumeric())) for coord in beacon]
    SENSORS[tuple(sensor)] = tuple(beacon)
    BEACONS.add(tuple(beacon))

distance = lambda t1, t2: abs(t1[0]-t2[0]) + abs(t1[1]-t2[1])

def impossible_beacons(row):
    EXCLUDED = set()
    for sensor, beacon in SENSORS.items():
        d = distance(sensor, beacon)
        x, y = sensor
        gap = d - abs(row-y) 
        for i in range(x-gap, x+gap+1):
                EXCLUDED.add(i)

    for beacon in SENSORS.values():
        x, y = beacon
        if y == row and x in EXCLUDED:
            EXCLUDED.remove(x)
    return EXCLUDED

excluded = impossible_beacons(10)
ans1 = len(excluded)
print(f'answer to first puzzle is: {ans1}')    

D = set()
for sensor, beacon in SENSORS.items():
    d = distance(sensor, beacon)
    D.add(d)

print(D)
ans2 = 0
print(f'answer to first puzzle is: {ans2}')
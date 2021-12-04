import os, sys

file_name = 'input_day_13.txt'
file_name = 'test_13.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    timestamp, timetable = f.read().split('\n') 
    
    def smallest_multiple_greater(x, n): 
        if x % n == 0: return x 
        return n * (x // n + 1)

    buses = [int(bus) for bus in timetable.split(',') if bus.isnumeric()]
    buses = sorted(buses, key = lambda n: smallest_multiple_greater(int(timestamp), n))
    ans1 = buses[0] * (smallest_multiple_greater(int(timestamp), buses[0]) - int(timestamp))
    print(f'answer to first puzzle of day {day} is: {ans1}')

    timetable = [(int(bus), i) for i, bus in enumerate(timetable.split(',')) if bus != 'x']
    gap = max(timetable, key = lambda x: x[0])
    ans2 = gap[0] + gap[1]
    while True:
        ans2 += gap[0]
        print(ans2)
        for bus, i in timetable:
            if (ans2 + i) % bus != 0: break
        if i == timetable[-1][1]: break

    print(f'answer to second puzzle of day {day} is: {ans2}')
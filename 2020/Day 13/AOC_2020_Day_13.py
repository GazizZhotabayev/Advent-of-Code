import os, sys

file_name = 'input_day_13.txt'
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

    timetable = [(int(bus), (int(bus)-i) % int(bus)) for i, bus in enumerate(timetable.split(',')) if bus != 'x']
    #chinese remainder theorem

    #https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving
    n, x = 1, timetable[0][1]
    while len(timetable) > 1:
        n *= timetable[0][0]
        timetable = timetable[1:]
        while True:
            if x % timetable[0][0] == timetable[0][1]: 
                break
            x += n

    ans2 = x
    print(f'answer to second puzzle of day {day} is: {ans2}')
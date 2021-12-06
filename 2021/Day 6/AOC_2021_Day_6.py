import os, sys
from collections import Counter

file_name = 'input_day_6.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    fishes = Counter([int(i) for i in f.read().split(',')])

    memory = {}
    #counts a single fish's offspring (and itself) 
    def count_fish(timer, days):
        try:
            return memory[(timer, days)]
        except:
            ans = count_fish(6, days - timer - 1) + count_fish(8, days - timer - 1) if days > timer else 1
            memory[(timer, days)] = ans
            return ans
    
    def count_school(school, days):
        return sum(n * count_fish(timer, days) for timer, n in school.items())

    ans1 = count_school(fishes, 80)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = count_school(fishes, 256)
    print(f'answer to second puzzle of day {day} is: {ans2}')
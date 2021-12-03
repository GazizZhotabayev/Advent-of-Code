import os, sys
from functools import reduce

file_name = 'input_day_4.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line.split('\n') for line in f.read().split('\n\n') if line != ''] 
    
    collate = lambda x: reduce(lambda l1, l2: l1+l2, x)

    lst = [collate([c.split() for c in passport]) for passport in lst]
    lst = [dict([tuple(field.split(':')) for field in passport]) for passport in lst]

    needed = set('byr iyr eyr hgt hcl ecl pid'.split())
    ans1 = sum(set(passport.keys()) >= needed for passport in lst)

    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = 0
    for passport in lst:
        byr = int(passport.get('byr', 0))
        iyr = int(passport.get('iyr', 0))
        eyr = int(passport.get('eyr', 0))
        hgt = passport.get('hgt', '')
        hcl = passport.get('hcl', '')
        ecl = passport.get('ecl', '')
        pid = passport.get('pid', '')

        if not (byr>=1920 and byr<=2002): continue
        if not (iyr>=2010 and iyr<=2020): continue
        if not (eyr>=2020 and eyr<=2030): continue 
        if not (hgt.endswith('cm') or hgt.endswith('in')): continue
        hgt, unit = int(hgt[:-2]), hgt[-2:]
        if not ( (unit=='cm' and (hgt>=150 and hgt<=193)) or (unit=='in' and (hgt>=59 and hgt<=76)) ): continue
        if not (hcl.startswith('#') and len(hcl) == 7 and hcl[1:].isalnum()): continue
        if not (ecl in 'amb blu brn gry grn hzl oth'.split()): continue
        if not (len(pid) == 9): continue
        ans2 += 1 
    
    print(f'answer to second puzzle of day {day} is: {ans2}')
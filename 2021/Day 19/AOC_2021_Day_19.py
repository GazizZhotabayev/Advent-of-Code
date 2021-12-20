import os, sys
import numpy as np

file_name = 'input_day_19.txt'
file_name = 'test_19.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    txt = [line for line in f.read().split('\n\n')]
    SCANNERS = {}
    for scanner in txt:
        scanner = scanner.split('\n')
        n = int(''.join(i for i in scanner[0] if i.isnumeric()))
        SCANNERS[n] = [[eval(line) for line in scanner[1:]]]
    
    r1 = lambda x,y,z: (x,y,z)
    r2 = lambda x,y,z: (x,z,-y)
    r3 = lambda x,y,z: (x,-z,y)
    r4 = lambda x,y,z: (x,y,z)
    r5 = lambda x,y,z: (x,y,z)
    r6 = lambda x,y,z: (x,y,z)
    r7 = lambda x,y,z: (x,y,z)
    r8 = lambda x,y,z: (x,y,z)
    r9 = lambda x,y,z: (x,y,z)
    r10 = lambda x,y,z: (x,y,z)
    r11 = lambda x,y,z: (x,y,z)
    r12 = lambda x,y,z: (x,y,z)
    r13 = lambda x,y,z: (x,y,z)
    r14 = lambda x,y,z: (x,y,z)
    r15 = lambda x,y,z: (x,y,z)
    r16 = lambda x,y,z: (x,y,z)
    r17 = lambda x,y,z: (x,y,z)
    r18 = lambda x,y,z: (x,y,z)
    r19 = lambda x,y,z: (x,y,z)
    r20 = lambda x,y,z: (x,y,z)
    r21 = lambda x,y,z: (x,y,z)
    r22 = lambda x,y,z: (x,y,z)
    r23 = lambda x,y,z: (x,y,z)
    r24 = lambda x,y,z: (x,y,z)


    ans1 = 0
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = 0
    print(f'answer to second puzzle of day {day} is: {ans2}')

import os, sys
import numpy as np
from numpy.lib import dsplit

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
    
    def rotate(p, M):
        x = np.matmul(M, np.array(p).reshape((3,1)))
        return tuple(x.reshape((1,3)).tolist()[0])

    def rotate_x(p):
        return rotate(p, np.array([[1,0,0], [0,0,-1], [0,1,0]]))

    def rotate_y(p):
        return rotate(p, np.array([[0,0,1], [0,1,0], [-1,0,0]]))

    def rotate_z(p):
        return rotate(p, np.array([[0,-1,0], [1,0,0], [0,0,1]]))

    def dist_vector(p1, p2):
        return tuple(p2[i] - p1[i] for i in range(3))

    ans1 = 0
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = 0
    print(f'answer to second puzzle of day {day} is: {ans2}')

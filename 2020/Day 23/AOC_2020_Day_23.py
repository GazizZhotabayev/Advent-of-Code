import os, sys
import numpy as np

day = 23

label = np.array([int(i) for i in '326519478'])

def move(x, current):
    picked_cups = label.take(range(current+1, current+4), mode='wrap')
    label = label

#print(label)
#print(len(label))

label.take(range(8,12), mode='wrap')
print(label)
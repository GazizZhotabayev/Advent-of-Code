import os, sys
from functools import cmp_to_key

file_name = 'input.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    pairs = f.read().split('\n\n')

with open(os.path.join(sys.path[0], file_name)) as f:
    packets = [eval(line) for line in f.read().split()]
    packets.append([[2]])
    packets.append([[6]])

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return -1
        if left < right:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        if left == right == []:
            pass
        else:
            try:
                l = left[0]
            except:
                return 1
            try:
                r = right[0]
            except:
                return -1

            x = compare(l, r)
            if x == 0:
                return compare(left[1:], right[1:])
            else:
                return x
    else:
        if isinstance(left, int): 
            return compare([left], right[:])
        elif isinstance(right, int): 
            return compare(left[:], [right])
        else:
            pass
    return 0

ans1 = 0
for i, pair in enumerate(pairs):
    left, right = [eval(p) for p in pair.split('\n')]
    if compare(left, right) == 1:
        ans1 += i+1

print(f'answer to first puzzle is: {ans1}')    

packets = sorted(packets, key = cmp_to_key(compare))[::-1]
ans2 = (packets.index([[2]])+1) * (packets.index([[6]])+1)
print(f'answer to first puzzle is: {ans2}')
import os, sys

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    original = [int(i) for i in f.read().split('\n')]

#original = [1, 2, -3, 3, -2, 0, 4]
#original = [0,4,5,1,2,2]

file = [(x, 0) for x in original]
for c in original:
    i = file.index((c, 0)) #current index of the character
    n = file.pop(i)[0]
    i = i + c #final index of the character
    if i % len(file) == 0:
        file.append((c, 1))
    else:
        if i > 0:
            i = i % len(file)
        else:
            i = i % len(file) - len(file)
        file.insert(i, (n, 1))
    #print(c, file)

i = file.index((0, 1))
ans1 = sum([file[(i+x)%len(file)][0] for x in [1000, 2000, 3000]])
print(f'answer to first puzzle is: {ans1}')    

original = [x * 811589153 for x in original]
file = [(x, 0) for x in original]
for round in range(10):
    for c in original:
        i = file.index((c, round)) #current index of the character
        n = file.pop(i)[0]
        i = i + c #final index of the character
        if i % len(file) == 0:
            file.append((c, round+1))
        else:
            if i > 0:
                i = i % len(file)
            else:
                i = i % len(file) - len(file)
            file.insert(i, (n, round+1))
    #print(round, file)

i = file.index((0, 10))
ans2 = sum([file[(i+x)%len(file)][0] for x in [1000, 2000, 3000]])
print(f'answer to first puzzle is: {ans2}')
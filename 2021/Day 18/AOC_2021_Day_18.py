import os, sys
from itertools import permutations

file_name = 'input_day_18.txt'
#file_name = 'test_18.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    SNAILFISH = [line for line in f.read().split('\n')]

    def add(snailfish1, snailfish2):
        return f'[{snailfish1},{snailfish2}]'

    def single_reduce(snailfish):

        #search for a pair to explode
        bracket_cnt = 0
        for i, c in enumerate(snailfish):
            
            if c == '[': bracket_cnt += 1
            if c == ']': bracket_cnt -= 1
            
            if bracket_cnt == 5 and c.isnumeric():
                
                i += -1 #want to capture the entire pair, with brackets
                j = i+snailfish[i:].index(']')
                n1, n2 = eval(snailfish[i:j+1]) #left and right numbers of the pair
                
                #next, search for the number immediately to the left of the pair
                for l in range(i, -1, -1):
                    if snailfish[l].isnumeric():
                        k = l
                        while k >= 0 and snailfish[k].isnumeric():
                            k += -1
                        break
                left = snailfish[:i] if l == 0 else snailfish[:k+1] + str(int(snailfish[k+1:l+1]) + n1) + snailfish[l+1:i]

                #now, search for the number immediately to the right of the pair
                for k in range(j+1, len(snailfish)):
                    if snailfish[k].isnumeric():
                        l = k
                        while l < len(snailfish) and snailfish[l].isnumeric():
                            l += 1
                        break
                right = snailfish[j+1:] if k == len(snailfish)-1 else snailfish[j+1:k] + str(int(snailfish[k:l]) + n2) + snailfish[l:]

                return left + '0' + right
                
        #if nothing to explode, search for a number to split
        for i, c in enumerate(snailfish):
            if c.isnumeric():
                j = i
                while snailfish[j].isnumeric():
                    j += 1
                n = snailfish[i:j]
                if len(n) > 1:
                    n1 = int(n) // 2
                    n2 = int(n) // 2 + 1 if int(n) % 2 == 1 else n1
                    return f'{snailfish[:i]}[{n1},{n2}]{snailfish[j:]}'
        
        #if no action, return as is
        return snailfish

    def reduce(snailfish):
        while True:
            r = single_reduce(snailfish)
            if r == snailfish:
                return snailfish
            else:
                snailfish = r 

    def magnitude(snailfish):
        if isinstance(snailfish, str): snailfish = eval(snailfish)
        if isinstance(snailfish, int): return snailfish
        left, right = snailfish[0], snailfish[-1]
        return 3 * magnitude(left) + 2 * magnitude(right)

    snailfish = SNAILFISH[0]
    for i in range(1, len(SNAILFISH)):
        snailfish = add(snailfish, SNAILFISH[i])
        snailfish = reduce(snailfish)

    ans1 = magnitude(snailfish)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    MAX_MAGNITUDE = 0
    for i, j in permutations(range(len(SNAILFISH)), 2):
        if i != j:
            x = magnitude(reduce(add(SNAILFISH[i], SNAILFISH[j])))
            if x > MAX_MAGNITUDE: MAX_MAGNITUDE = x

    ans2 = MAX_MAGNITUDE
    print(f'answer to second puzzle of day {day} is: {ans2}')

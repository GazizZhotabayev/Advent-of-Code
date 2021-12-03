import os, sys
from collections import Counter

file_name = 'input_day_3.txt'
with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [i for i in f.read().split('\n') if i != '']

    #transpose list of strings
    transpose = lambda x: [''.join(line[i] for line in x) for i in range(len(x[0]))]
    
    #get the most common value in lst (with tiebreaker rules)
    g = lambda x: '1' if x.count('1') >= x.count('0') else '0'
    e = lambda x: '0' if x.count('1') >= x.count('0') else '1'

    gamma = ''.join(g(line) for line in transpose(lst))
    epsilon = ''.join('1' if i == '0' else '0' for i in gamma)

    print(f'answer to first puzzle of day 3 is: {int(gamma, 2) * int(epsilon, 2)}')

    oxygen_lst = lst[:]
    co2_lst = lst[:]

    i = 0
    while len(oxygen_lst) > 1:
        most_common = g(transpose(oxygen_lst)[i])
        oxygen_lst = [n for n in oxygen_lst if n[i] == most_common]
        i += 1

    i = 0
    while len(co2_lst) > 1:
        least_common = e(transpose(co2_lst)[i])
        co2_lst = [n for n in co2_lst if n[i] == least_common]
        i += 1
    
    print(f'answer to first puzzle of day 3 is: {int(oxygen_lst[0], 2) * int(co2_lst[0], 2)}')
import os, sys

file_name = 'input.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    instructions = f.read().split('\n')

ans1 = 0
print(f'answer to first puzzle is: {ans1}')

ans2 = 0
print(f'answer to second puzzle is: {ans2}')
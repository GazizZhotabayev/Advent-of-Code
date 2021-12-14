import os, sys

file_name = 'input_day_20.txt'
file_name = 'test_20.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    tiles = f.read().split('\n\n')
    tiles = {tile.split('\n')[0].split()[-1][:-1]: tile.split('\n')[1:] for tile in tiles}
    tiles = {n: [list(row) for row in tile] for n, tile in tiles.items()}

    def 
    print(tiles)
    ans1 = 0
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = 0
    print(f'answer to second puzzle of day {day} is: {ans2}')
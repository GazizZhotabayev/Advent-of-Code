import os, sys

file_name = 'input_day_20.txt'
#file_name = 'test_20.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    ALGO, IMG = f.read().split('\n\n')
    IMG = [list(line) for line in IMG.split('\n')]

    #extend image to (2*n + current length) x (2*n + current length)
    n = 200
    IMG = [['.' for i in range(n)] + line + ['.' for i in range(n)] for line in IMG]
    row = ['.' for i in range(2 * n + len(IMG))]
    IMG = [row for i in range(n)] + IMG + [row for i in range(n)]

    def transform(img, x, y, algo):
        try:
            s = ''.join(''.join(img[i][j] for j in range(y-1,y+2)) for i in range(x-1,x+2))
            s = int(''.join('1' if i == '#' else '0' for i in s), 2)
            return algo[s]
        except:
            return '.'

    def enhance(img, algo):
        return [[transform(img, x, y, algo) for y in range(len(img))] for x in range(len(img))]

    def count_lit(img):
        return sum(sum(1 for y in range(len(img)) if img[x][y] == '#') for x in range(len(img)))

    #count lit pixels only on the nxn innermost square inside of an image 
    def count_lit_inner(img, n):
        L = len(img)
        m = (L - n) // 2
        return count_lit([[img[i][j] for j in range(m, m+n)] for i in range(m, m+n)])

    ANS = []
    for step in range(50):
        IMG = enhance(IMG, ALGO)
        ANS.append(count_lit_inner(IMG, 220))
    
    ans1 = ANS[1]
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = ANS[49]
    print(f'answer to second puzzle of day {day} is: {ans2}')

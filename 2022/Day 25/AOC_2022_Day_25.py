import os, sys

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    lines = f.read().split('\n')

FROM_SNAFU = {k:v for k, v in zip('=-012', range(-2,3))}
TO_SNAFU = {k:v for k, v in zip(range(-2,3), '=-012')}

def snafu_to_decimal(x):
    return sum(FROM_SNAFU[k] * 5 ** (len(x)-1-i) for i, k in enumerate(x))

def decimal_to_base5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n = n // 5
    return [int(i) for i in s]

def update_base5(s):
    while 5 in s:
        for i, c in enumerate(s[::-1]):
            if c == 5:
                if i == len(s)-1:
                    s = [1,0] + s[1:]
                else:
                    s[len(s)-1-i] = 0
                    s[len(s)-2-i] += 1
                break
            else:
                pass
    return s

def decimal_to_snafu(n):
    s = decimal_to_base5(n)
    x = []
    while s:
        c = s.pop(-1)
        if 3<=c<=4:
            if c == 3: x.append('=')
            if c == 4: x.append('-')
            s[-1] += 1
            s = update_base5(s)
        else:
            x.append(c)
    return ''.join(str(i) for i in x)[::-1]

x = sum(snafu_to_decimal(line) for line in lines)
ans1 = decimal_to_snafu(x)

print(f'answer to first puzzle is: {ans1}')    

ans2 = 0
print(f'answer to first puzzle is: {ans2}')
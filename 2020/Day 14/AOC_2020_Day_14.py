import os, sys, re

file_name = 'input_day_14.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line for line in f.read().split('\n')] 
    
    def transform(mask, n):
        b = bin(n)[2:].zfill(len(mask))
        b = ''.join(c if c != 'X' else b[i] for i, c in enumerate(mask))
        return int(b, 2)
    
    mem = dict()
    for line in lst:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        elif line.startswith('mem'):
            address, value = int(re.findall('\[(.*?)\]', line)[0]), int(line.split(' = ')[1])
            mem[address] = transform(mask, value)
        else:
            pass

    ans1 = sum(mem.values())
    print(f'answer to first puzzle of day {day} is: {ans1}')

    def transform_address(mask, n):
        b = bin(n)[2:].zfill(len(mask))
        b = ''.join('1' if c == '1' else b[i] if c == '0' else c for i, c in enumerate(mask))
        ans = [b]
        while not all(c.isnumeric() for c in ans):
            for i, x in enumerate(ans):
                try:
                    j = x.index('X')
                    b1 = x[:j] + '0' + x[j+1:]
                    b2 = x[:j] + '1' + x[j+1:]
                    ans.remove(x)
                    ans += [b1, b2]
                    break
                except:
                    pass
        return [int(b, 2) for b in ans]

    mem = dict()
    for line in lst:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        elif line.startswith('mem'):
            address, value = int(re.findall('\[(.*?)\]', line)[0]), int(line.split(' = ')[1])
            addresses = transform_address(mask, address)
            for address in addresses:
                mem[address] = value
        else:
            pass

    ans2 = sum(mem.values())
    print(f'answer to second puzzle of day {day} is: {ans2}')
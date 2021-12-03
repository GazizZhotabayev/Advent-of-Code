import os, sys

file_name = 'input_day_8.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line.split() for line in f.read().split('\n') if line != ''] 

    def execute(lst):
        i, visited, acc = 0, set(), 0
        while True:
            visited.add(i)
            cmd, n = lst[i]
            if cmd == 'nop': 
                i += 1
            if cmd == 'jmp':
                i += int(n)
            elif cmd == 'acc':
                acc += int(n)
                i += 1
            else: 
                pass

            if i in visited or i == len(lst): break
        
        return acc, i
        
    ans1 = execute(lst)
    print(f'answer to first puzzle of day {day} is: {ans1[0]}')

    max_cmd = len(lst)
    for i, line in enumerate(lst):
        if line[0] == 'jmp':  
            ans2 = execute(lst[:i] + [['nop', line[1]]] + lst[i+1:])
        elif line[0] == 'nop':  
            ans2 = execute(lst[:i] + [['jmp', line[1]]] + lst[i+1:])
        else:
            continue

        if ans2[-1] == max_cmd: break
    
    print(f'answer to second puzzle of day {day} is: {ans2[0]}')
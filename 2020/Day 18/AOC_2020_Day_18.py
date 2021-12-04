import os, sys, re

file_name = 'input_day_18.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line for line in f.read().split('\n') if line != ''] 

    def simple_evaluate(line):
        line = line.replace('(','').replace(')','').split()
        n = int(line[0])
        i = 1
        while i < len(line) - 1:
            n = n + int(line[i+1]) if line[i] == '+' else n * int(line[i+1])
            i += 2
        return str(n)
    
    def simplify_parentheses(line):
        innermost_parentheses = re.findall("\([^()]+\)", line)
        for pair in innermost_parentheses:
            line = line.replace(pair, simple_evaluate(pair))
        return line

    def evaluate(line):
        while '(' in line: 
            line = simplify_parentheses(line)
        if '+' in line or '*' in line:
            n = simple_evaluate(line)
        else:
            n = line
        return n

    ans1 = [int(evaluate(line)) for line in lst]
    print(f'answer to first puzzle of day {day} is: {sum(ans1)}')

    def simple_addition_first(line):
        line = line.replace('(','').replace(')','').split()
        while '+' in line:
            i = line.index('+')
            n = int(line[i-1]) + int(line[i+1])
            line = line[:i-1] + [str(n)] + line[i+2:]

        while '*' in line:
            i = line.index('*')
            n = int(line[i-1]) * int(line[i+1])
            line = line[:i-1] + [str(n)] + line[i+2:]

        return str(n)
    
    def simplify_parentheses_addition_first(line):
        innermost_parentheses = re.findall("\([^()]+\)", line)
        for pair in innermost_parentheses:
            line = line.replace(pair, simple_addition_first(pair))
        return line

    def evaluate_addition_first(line):
        while '(' in line: 
            line = simplify_parentheses_addition_first(line)
        if '+' in line or '*' in line:
            n = simple_addition_first(line)
        else:
            n = line
        return n

    ans2 = [int(evaluate_addition_first(line)) for line in lst]
    print(f'answer to second puzzle of day {day} is: {sum(ans2)}')
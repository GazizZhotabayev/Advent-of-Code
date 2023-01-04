import os, sys, re
from sympy import solve, sympify

file_name = 'input.txt'

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [tuple(x.split(': ')) for x in f.read().split('\n')]

def build_dictionary(monkeys):
    MONKEYS = dict()
    while monkeys:
        for monkey, rule in monkeys:
            if rule.isnumeric():
                MONKEYS[monkey] = int(rule)
                monkeys.remove((monkey, rule))
            else:
                try:
                    m1, o, m2 = rule.split() 
                    MONKEYS[monkey] = eval(f"{MONKEYS[m1]}{o}{MONKEYS[m2]}")
                    monkeys.remove((monkey, rule))
                except:
                    pass
    return MONKEYS

ans1 = build_dictionary(lst[:])['root']
print(f'answer to first puzzle is: {ans1}')    

def create_formula(monkeys, monkey):
    pattern = r'([a-z]+)'
    formula = next(t[1] for t in monkeys if t[0] == monkey)
    while True:
        formula = re.sub(pattern, '(\g<1>)', formula)
        formula = [c for c in re.split('([^a-zA-Z])', formula) if len(c) > 0]
        for i, x in enumerate(formula):
            if x.isalpha():
                formula[i] = next(t[1] for t in monkeys if t[0] == x)
        formula = ''.join(formula)
        check = formula.replace('humn', '')
        if all(not(x.isalpha()) for x in check):
            return formula

def simplify(formula):
    pattern = r'(\([^\(\)]+\))'
    while True:
        original = formula
        formula = re.split(pattern, formula)
        for i, x in enumerate(formula):
            try:
                formula[i] = str(int(eval(x)))
            except:
                pass
        formula = ''.join(formula)
        if formula == original:
            return formula

x = next(i for i, t in enumerate(lst) if t[0] == 'humn')
lst[x] = ('humn', 'humn')

E1, o, E2 = next(t for t in lst if t[0] == 'root')[1].split()
E1 = simplify(create_formula(lst[:], E1)).replace('humn', 'x')
E2 = simplify(create_formula(lst[:], E2)).replace('humn', 'x')

equation = f'Eq({E1},{E2})'

ans2 = solve(equation)[0]
print(f'answer to first puzzle is: {ans2}')
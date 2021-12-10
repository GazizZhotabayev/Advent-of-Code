import os, sys, re

file_name = 'input_day_10.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line for line in f.read().split('\n')]
    
    pattern = re.compile(r'(\<\>|\{\}|\(\)|\[\])')
    closed_brackets = re.compile(r'(\>|\}|\)|\])')

    def parse_line(line):
        while bool(re.search(pattern, line)):
            line = re.sub(pattern, '', line)
        line_type = 'corrupted' if bool(re.search(closed_brackets, line)) else 'correct' if line == '' else 'incomplete'
        first_closed = re.findall(closed_brackets, line)[0] if line_type == 'corrupted' else ''
        return line, line_type, first_closed

    ans1 = 0
    SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for line in lst:
        line, line_type, first_closed = parse_line(line)
        ans1 += SCORES.get(first_closed, 0)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    lst = [parse_line(line) for line in lst]
    lst = [line[0] for line in lst if line[1] == "incomplete"]
    SCORES2 = {')': 1, ']': 2, '}': 3, '>': 4}
    REVERSE = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def score_incomplete(line):
        total_score = 0
        for c in line[::-1]:
            total_score *= 5
            total_score += SCORES2[REVERSE[c]]
        return total_score

    ans2 = sorted([score_incomplete(line) for line in lst])[len(lst) // 2]
    print(f'answer to second puzzle of day {day} is: {ans2}')
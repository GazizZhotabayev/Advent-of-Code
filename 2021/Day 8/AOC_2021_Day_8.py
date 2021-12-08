import os, sys

file_name = 'input_day_8.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line for line in f.read().split('\n')]
    
    ans1 = 0
    for line in lst:
        pattern, value = line.split(' | ')
        pattern, value = pattern.split(), value.split()    
        ans1 += sum(1 for digit in value if len(set(digit)) in (2, 3, 4, 7))
    print(f'answer to first puzzle of day {day} is: {ans1}')
    
    def parse_line(line):
        DIGITS, LETTERS = dict(), dict()
        pattern, value = line.split(' | ')
        pattern, value = pattern.split(), value.split()    
        DIGITS[1] = [digit for digit in pattern if len(digit) == 2][0]
        DIGITS[4] = [digit for digit in pattern if len(digit) == 4][0]
        DIGITS[7] = [digit for digit in pattern if len(digit) == 3][0]
        DIGITS[8] = [digit for digit in pattern if len(digit) == 7][0]

        LETTERS['top'] = [letter for letter in DIGITS[7] if letter not in DIGITS[1]][0]
        LETTERS['top right'] = [letter for letter in 'abcdefg' if sum(1 for digit in pattern if letter in digit) == 8 and letter != LETTERS['top']][0]
        LETTERS['top left'] = [letter for letter in 'abcdefg' if sum(1 for digit in pattern if letter in digit) == 6][0]
        LETTERS['bottom left'] = [letter for letter in 'abcdefg' if sum(1 for digit in pattern if letter in digit) == 4][0]
        LETTERS['bottom right'] = [letter for letter in 'abcdefg' if sum(1 for digit in pattern if letter in digit) == 9][0]
        LETTERS['middle'] = [letter for letter in 'abcdefg' if letter in DIGITS[4] and sum(1 for digit in pattern if letter in digit) == 7][0]
        LETTERS['bottom'] = [letter for letter in 'abcdefg' if letter not in LETTERS.values()][0]

        DIGITS[0] = ''.join(letter for pos, letter in LETTERS.items() if pos != 'middle')
        DIGITS[2] = ''.join(letter for pos, letter in LETTERS.items() if pos not in ('top left', 'bottom right'))
        DIGITS[3] = ''.join(letter for pos, letter in LETTERS.items() if pos not in ('top left', 'bottom left'))
        DIGITS[5] = ''.join(letter for pos, letter in LETTERS.items() if pos not in ('top right', 'bottom left'))
        DIGITS[6] = ''.join(letter for pos, letter in LETTERS.items() if pos != 'top right')
        DIGITS[9] = ''.join(letter for pos, letter in LETTERS.items() if pos != 'bottom left')

        REVERSED_DIGITS = {''.join(sorted(letters)): str(digit) for digit, letters in DIGITS.items()}
        return ''.join(REVERSED_DIGITS[''.join(sorted(letters))] for letters in value)


    ans2 = sum(int(parse_line(line)) for line in lst)
    print(f'answer to second puzzle of day {day} is: {ans2}')
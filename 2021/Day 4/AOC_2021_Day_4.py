import os, sys

file_name = 'input_day_4.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    txt = f.read()
    order = [int(i) for i in txt.split('\n\n')[0].split(',')]
    boards = [[[int(i) for i in subline.split()] for subline in line.split('\n')] for line in txt.split('\n\n')[1:] ]

    def update_board(board, n):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == n: board[i][j] = -1
        return board

    transpose_board = lambda board: [[board[j][i] for j in range(len(board))] for i in range(len(board))]
        
    def check_board(board):
        return any(set(row) == set([-1]) for row in board) or any(set(col) == set([-1]) for col in transpose_board(board))

    stop = False
    boards_that_won = []
    ans1, ans2 = None, None

    for n in order:
        for i, board in enumerate(boards):
            board = update_board(board, n)
            if check_board(board):
                if ans1 is None: ans1 = n * sum(sum(i for i in row if i != -1) for row in board)
                if i not in boards_that_won: boards_that_won += [i]
                if len(boards_that_won) == len(boards):
                    if ans2 is None: ans2 = n * sum(sum(i for i in row if i != -1) for row in board)

    print(f'answer to first puzzle of day {day} is: {ans1}')
    
    print(f'answer to second puzzle of day {day} is: {ans2}')
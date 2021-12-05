import os, sys

file_name = 'input_day_22.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    player1, player2 = f.read().split('\n\n')
    player1, player2 = [int(i) for i in player1.split('\n')[1:]], [int(i) for i in player2.split('\n')[1:]] 

    def game(p1, p2):
        while len(p1) * len(p2) > 0:
            c1, c2 = p1.pop(0), p2.pop(0)
            if c1 > c2:
                p1 += [c1, c2]
            if c2 > c1:
                p2 += [c2, c1]
        
        winner = p1 if len(p1) > 0 else p2
        return winner

    ans1 = sum((i+1)*c for i, c in enumerate(game(player1[:], player2[:])[::-1]))
    print(f'answer to first puzzle of day {day} is: {ans1}')

    def recursive_game(p1, p2):
        rounds, stop = [], False

        while len(p1) * len(p2) > 0:
            print(p1,p2)
            c1, c2 = p1.pop(0), p2.pop(0)
            if c1 >= len(p1) and c2 >= len(p2):
                return recursive_game(p1, p2)
        
            if c1 > c2:
                p1 += [c1, c2]
            if c2 > c1:
                p2 += [c2, c1]
            
            for round in rounds:
                if p1 == round[0] and p2 == round[1]:
                    stop = True
                    break
            if stop: return p1
            rounds.append([p1, p2])
        
        winner = p1 if len(p1) > 0 else p2
        return winner
    
    ans2 = sum((i+1)*c for i, c in enumerate(recursive_game(player1[:], player2[:])[::-1]))
    print(f'answer to second puzzle of day {day} is: {ans2}')
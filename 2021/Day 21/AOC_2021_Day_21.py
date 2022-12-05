from collections import Counter

day = 21

p1, p2 = 7, 10
s1, s2 = 0, 0

die = [1, 2, 3]
total_turns, turn = 0, 0
while max((s1,s2)) < 1000:
    d = sum(die)
    if turn % 2 == 0:
        p1 = (p1 + d) % 10 if (p1 + d) % 10 != 0 else 10
        s1 += p1
    else:
        p2 = (p2 + d) % 10 if (p2 + d) % 10 != 0 else 10
        s2 += p2

    #print(f'The die were: {die} for a total of {d} - player 1 has {s1} and is on {p1}, player 2 has {s2} and is on {p2}')
    die = [(i+3) % 100 if (i+3) != 100 else 100 for i in die]
    total_turns += 1
    turn = (turn + 1) % 2

ans1 = min((s1, s2)) * total_turns * 3
print(f'answer to first puzzle of day {day} is: {ans1}')

DIRAC = Counter([i+j+k for i in range(1,4) for j in range(1,4) for k in range(1,4)])
STATES = {}
def simulate_game(p1, p2, s1, s2, turn):

    state = (p1, p2, s1, s2, turn)
    if state in STATES: return STATES[state]

    if s1 > 20: 
        STATES[state] = [1,0]
        return [1,0]
    if s2 > 20: 
        STATES[state] = [0,1]
        return [0,1] 
    
    STATES[state] = [0,0]
    for d, v in DIRAC.items():
        if turn % 2 == 0:
            p1_new = (p1 + d) % 10 if (p1 + d) % 10 != 0 else 10
            s1_new = s1 + p1_new
            p2_new, s2_new = p2, s2
        else:
            p2_new = (p2 + d) % 10 if (p2 + d) % 10 != 0 else 10
            s2_new = s2 + p2_new
            p1_new, s1_new = p1, s1
        
        p1_wins, p2_wins = simulate_game(p1_new, p2_new, s1_new, s2_new, (turn+1) % 2)
        STATES[state][0] += p1_wins * v
        STATES[state][1] += p2_wins * v
    
    return STATES[state]
    
state = (7, 10, 0, 0, 0)
simulate_game(*state)
ans2 = max(STATES[state])
print(f'answer to second puzzle of day {day} is: {ans2}')
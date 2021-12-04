import os, sys
from functools import reduce

file_name = 'input_day_16.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    lst = [line for line in f.read().split('\n\n') if line != ''] 

    def parse_field(field):
        rng = field.split(': ')[1]
        rng1 = rng.split(' or ')[0].lstrip(' ').split('-')
        rng2 = rng.split(' or ')[1].split('-')
        return list(range(int(rng1[0]), int(rng1[1]) + 1)) + list(range(int(rng2[0]), int(rng2[1]) + 1))

    fields = {field.split(':')[0]: parse_field(field) for field in lst[0].split('\n')}

    tickets = [[int(i) for i in ticket.split(',')] for ticket in lst[-1].split('\n')[1:]]

    collate = lambda x: reduce(lambda l1, l2: l1+l2, x)
    all_valid_values = set(collate([v for k, v in fields.items()]))
    all_ticket_values = collate(tickets)

    ans1 = [v for v in all_ticket_values if v not in all_valid_values]
    print(f'answer to first puzzle of day {day} is: {sum(ans1)}')

    valid_ticket = lambda ticket: all(v in all_valid_values for v in ticket)
    tickets = [ticket for ticket in tickets if valid_ticket(ticket)]

    field_positions = {field: [] for field in fields}
    possible_positions = range(len(tickets[0]))
    while not all(len(v) == 1 for k, v in field_positions.items()):
        for field in fields:
            for i in possible_positions:
                if all(ticket[i] in fields[field] for ticket in tickets):
                    field_positions[field].append(i)

        identified_positions = [v[0] for k, v in field_positions.items() if len(v) == 1]
        possible_positions = [i for i in range(len(tickets[0])) if i not in identified_positions]
        field_positions = {field: v if len(v) == 1 else [] for field, v in field_positions.items()}
    
    my_ticket = [int(i) for i in lst[1].split('\n')[1].split(',')]
    departure_positions = [pos[0] for field, pos in field_positions.items() if field.startswith('departure')]
    multiply = lambda x: reduce(lambda a, b: a*b, x)
    ans2 = multiply([my_ticket[pos] for pos in departure_positions])
    print(f'answer to second puzzle of day {day} is: {ans2}')
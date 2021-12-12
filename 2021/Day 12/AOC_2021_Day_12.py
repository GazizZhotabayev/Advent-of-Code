import os, sys
from itertools import groupby

file_name = 'input_day_12.txt'
day = file_name.split('.')[0].split('_')[-1]

#https://stackoverflow.com/questions/62656477/python-get-all-paths-from-graph
with open(os.path.join(sys.path[0], file_name)) as f:
    edges = [line.split('-') for line in f.read().split('\n')]
    caves = list(set([edge[0] for edge in edges] + [edge[1] for edge in edges]))
    
    EDGES = {cave: [edge[0] for edge in edges if cave == edge[1]] + [edge[1] for edge in edges if cave == edge[0]] for cave in caves}
    PATHS = [[]]
    
    def find_paths(current, visited):
        visited.append(current)
        for cave in EDGES[current]:
            if cave.isupper() or cave not in visited:
                find_paths(cave, visited.copy())
        PATHS.append(visited)

    def trim_path(path, cave):
        try:
            i = path.index(cave)
            return path[:i+1]
        except:
            return []

    find_paths('start', [])
    PATHS = [trim_path(path, 'end') for path in PATHS]
    PATHS = sorted([path for path in PATHS if len(path) > 0])
    PATHS = [path for path, g in groupby(PATHS)]
    
    ans1 = len(PATHS)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    PATHS = [[]]
    def find_paths_2(current, visited, double_visit):
        visited.append(current)
        for cave in EDGES[current]:
            if cave.isupper() or cave not in visited:
                find_paths_2(cave, visited.copy(), double_visit)
            elif cave not in ('start', 'end') and double_visit == False:
                find_paths_2(cave, visited.copy(), True)
        PATHS.append(visited)

    find_paths_2('start', [], False)
    PATHS = [trim_path(path, 'end') for path in PATHS]
    PATHS = sorted([path for path in PATHS if len(path) > 0])
    PATHS = [path for path, g in groupby(PATHS)]
    
    ans2 = len(PATHS)
    print(f'answer to second puzzle of day {day} is: {ans2}')
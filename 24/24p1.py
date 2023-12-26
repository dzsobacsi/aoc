import numpy as np
from itertools import combinations

TEST_MIN = 200000000000000  #7
TEST_MAX = 400000000000000  #27
INPFILE = 'input.txt'

def is_in_test_area(sol):
    return np.all(sol >= TEST_MIN) and np.all(sol <= TEST_MAX)

def is_in_future(a, b, sol):
    ax = (sol[0] - a['p'][0]) * a['v'][0] > 0
    ay = (sol[1] - a['p'][1]) * a['v'][1] > 0
    bx = (sol[0] - b['p'][0]) * b['v'][0] > 0
    by = (sol[1] - b['p'][1]) * b['v'][1] > 0
    return all([ax, ay, bx, by])

input = []
with open(INPFILE) as file:
    for line in file:
        p, v = line.strip().split('@')
        px, py, pz = [int(x.strip()) for x in p.split(',')]
        vx, vy, vz = [int(x.strip()) for x in v.split(',')]
        input.append({
            'p': [px, py, pz],
            'v': [vx, vy, vz]
        })

    for i in input:
        i['a1'] = i['v'][1] / i['v'][0]
        i['a2'] = -1
        i['b'] = i['a1'] * i['p'][0] - i['p'][1]

result = 0
for a, b in combinations(input, 2):
    A = np.array([[a['a1'], a['a2']], [b['a1'], b['a2']]])
    if np.linalg.det(A):
        B = np.array([a['b'], b['b']])
        solution = np.linalg.solve(A, B)
        if is_in_test_area(solution) and is_in_future(a, b, solution):
            result += 1
        #print(solution, end=' - ')
        #print('in' if is_in_test_area(solution) else 'out', end=' - ')
        #print('future' if is_in_future(a, b, solution) else 'past')
    else:
        pass#print('singular')

print(result)

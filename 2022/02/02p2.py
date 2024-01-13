"""
A for Rock,
B for Paper,
C for Scissors

X for Rock,     loose,
Y for Paper,    draw,
Z for Scissors, win
"""

result = 0

win_mtx = {
    'A': [3, 1, 2],
    'B': [1, 2, 3],
    'C': [2, 3, 1]
}

win_points = {
    'Z': 6,
    'Y': 3,
    'X': 0
}

order = {
    'X': 0,
    'Y': 1,
    'Z': 2
}

def get_points(a, b):
    result = 0
    result += win_points[b]
    result += win_mtx[a][order[b]]
    return result

with open('input.txt', 'r') as file:
    for line in file:
        a, b = line.strip().split()
        result += get_points(a, b)


print(result)

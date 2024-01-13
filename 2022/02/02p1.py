"""
A for Rock,
B for Paper,
C for Scissors

X for Rock,
Y for Paper,
Z for Scissors
"""

result = 0

winners = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

draws = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

shape = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def get_points(a, b):
    result = 0
    if winners[a] == b:
        result += 6
    if draws[a] == b:
        result += 3
    result += shape[b]
    return result

with open('input.txt', 'r') as file:
    for line in file:
        a, b = line.strip().split()
        result += get_points(a, b)

print(result)

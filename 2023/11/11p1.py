import re
from itertools import combinations

input = []
galaxies = []
result = 0

with open('input.txt') as file:
    for line in file:
        input.append(line.strip())

for i, line in enumerate(input):
    res = re.finditer('#', line)
    for r in res:
        galaxies.append((i, r.start()))

di = 0
for i in range(len(input)):
    if len([g for g in galaxies if g[0] == i + di]) == 0:
        galaxies = [(g[0] + 1, g[1]) if g[0] > i + di else g for g in galaxies]
        di += 1

dj = 0
for j in range(len(input[0])):
    if len([g for g in galaxies if g[1] == j + dj]) == 0:
        galaxies = [[g[0], g[1] + 1] if g[1] > j + dj else g for g in galaxies]
        dj += 1

for a, b in combinations(galaxies, 2):
    result += abs(a[0] - b[0]) + abs(a[1] - b[1])

print(result)

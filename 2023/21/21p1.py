map = []
with open('small.txt') as file:
    for line in file:
        map.append(list(line.strip()))

visited = set()
STEPNUM = 6

for i, row in enumerate(map):
    for j, x in enumerate(row):
        if x == 'S':
            visited.add((i, j))
            map[i][j] = '.'
            break

for _ in range(STEPNUM):
    new_points = set()
    for i in visited:
        for j in [(i[0]+1, i[1]), (i[0], i[1]+1), (i[0]-1, i[1]), (i[0], i[1]-1)]:
            if map[j[0]][j[1]] == '.':
                new_points.add(j)
    visited = new_points.copy()
    print(visited)

print(len(visited))
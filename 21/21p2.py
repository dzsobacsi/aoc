import time
start = time.time()

map = []
with open('input.txt') as file:
    for line in file:
        map.append(list(line.strip()))

visited_0 = set()
visited_1 = set()
visited_2 = set()
h = len(map)
w = len(map[0])
STEPNUM = 500

def bootstrap():
    for i, row in enumerate(map):
        for j, x in enumerate(row):
            if x == 'S':
                visited_0.add((i, j))
                map[i][j] = '.'
                break


def make_one_step():
    global visited_0, visited_1, visited_2, h, w
    new_points = set()
    for i in visited_0.difference(visited_2):
        for j in [(i[0]+1, i[1]), (i[0], i[1]+1), (i[0]-1, i[1]), (i[0], i[1]-1)]:
            if map[j[0] % h][j[1] % w] == '.':
                new_points.add(j)
    temp = visited_1.union(new_points)
    visited_2 = visited_1
    visited_1 = visited_0
    visited_0 = temp
    #print(visited_0)

bootstrap()
for _ in range(STEPNUM):
    make_one_step()

print(len(visited_0))
print(time.time() - start)


import sys
#import faulthandler

#faulthandler.enable()

sys.setrecursionlimit(10000000)

input = []

with open('input.txt') as file:
    for line in file:
        dir, x, col = line.split()
        input.append((dir, int(x)))

maxx = 0
maxy = 0
minx = 0
miny = 0
x = 0
y = 0
for dir, num in input:
    if dir == 'R':
        x += num
        maxx = max(x, maxx)
    if dir == 'D':
        y += num
        maxy = max(y, maxy)
    if dir == 'L':
        x -= num
        minx = min(x, minx)
    if dir == 'U':
        y -= num
        miny = min(y, miny)

print(minx, maxx)
print(miny, maxy)

map = []
for y in range(maxy - miny + 1):
    map.append(list('.' * (maxx - minx + 1)))

def printmap():
    for i in map:
        print(''.join(i))

x = -minx
y = -miny
map[y][x] = '#'
for dir, num in input:
    for i in range(num):
        if dir == 'R':
            x += 1
        if dir == 'D':
            y += 1
        if dir == 'L':
            x -= 1
        if dir == 'U':
            y -= 1
        map[y][x] = '#'


def flood_fill(y=1, x=1):
    print(y,x)
    if map[y][x] == '#':
        return
    map[y][x] = '#'
    flood_fill(y, x + 1)
    flood_fill(y + 1, x)
    flood_fill(y, x - 1)
    flood_fill(y - 1, x)
    return

#flood_fill(1, map[1].index('#') + 2)

result = 0
for i in map:
    result += i.count('#')


printmap()
print(result)

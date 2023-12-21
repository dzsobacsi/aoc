map = []

with open('input.txt') as file:
    for line in file:
        map.append(list(line.strip()))


def find_starting_position(map):
    for i, row in enumerate(map):
        if 'S' in row:
            return [i, row.index('S')]


def find_starting_direction(map, pos):
    dirs = set(('N', 'S', 'W', 'E'))
    y, x = pos
    if map[y-1][x] in '-LJ.' or y == 0:
        dirs.remove('N')
    if map[y+1][x] in '-7F.' or y == len(map) - 1:
        dirs.remove('S')
    if map[y][x-1] in '|J7.' or x == 0:
        dirs.remove('W')
    if map[y][x+1] in '|LF.' or x == len(map[0]) - 1:
        dirs.remove('E')
    return dirs.pop()


def to(map, pos, dir):
    y, x = pos
    if map[y][x] == '|':
        return 'N' if dir != 'S' else 'S'
    if map[y][x] == '-':
        return 'E' if dir != 'W' else 'W'
    if map[y][x] == 'L':
        return 'N' if dir != 'S' else 'E'
    if map[y][x] == 'J':
        return 'N' if dir != 'S' else 'W'
    if map[y][x] == '7':
        return 'S' if dir != 'N' else 'W'
    if map[y][x] == 'F':
        return 'S' if dir != 'N' else 'E'
    if map[y][x] == 'S':
        print('Horray')
        return None
    else:
        raise ValueError('Wrong map position')


def update_position(pos, dir):
    y, x = pos
    if dir == 'N':
        return [y-1, x]
    if dir == 'S':
        return [y+1, x]
    if dir == 'W':
        return [y, x-1]
    if dir == 'E':
        return [y, x+1]
    else:
        raise ValueError('Wrong direction')


start = find_starting_position(map)
pos = start.copy()
dir = find_starting_direction(map, pos)
steps = 0

while not (pos == start and steps > 0):
    pos = update_position(pos, dir)
    dir = to(map, pos, dir)
    steps += 1

print(steps//2)

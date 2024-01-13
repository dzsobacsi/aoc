import numpy as np

bricks = []
with open('input.txt') as file:
    for line in file:
        a, b = line.strip().split('~')
        bricks.append(tuple(int(x) for x in (*a.split(','), *b.split(','))))

def add_remove_brick_to_world(b, s):
    if s not in ['add', 'remove']:
        raise ValueError('Second argument must be either "add" or "remove"')
    world[b[0] : b[3]+1, b[1] : b[4]+1, b[2] : b[5]+1] = 1 if s == 'add' else 0

def can_go_lower(b):
    if b[2] == 0:
        return False
    return np.all(world[b[0] : b[3]+1, b[1] : b[4]+1, b[2]-1] == 0)

def move_lower(b):
    idx = np.where((bricks == b).all(axis=1))[0][0]
    #print('moving lower: ', idx, b)
    b_new = b.copy()
    b_new[[2, 5]] -= 1
    add_remove_brick_to_world(b, 'remove')
    add_remove_brick_to_world(b_new, 'add')
    bricks[idx, [2, 5]] -= 1
    return bricks[idx]


#Store bricks such that z starts with 0 instead of 1
bricks.sort(key=lambda x: x[2])
bricks = np.array(bricks)
bricks[:, [2, 5]] -= 1

#Create an empty world
maxx = np.max(bricks[:, 3]) + 1
maxy = np.max(bricks[:, 4]) + 1
maxz = np.max(bricks[:, 5]) + 1
world = np.zeros((maxx, maxy, maxz), dtype='int32')

#Fill the world with bricks
for b in bricks:
    add_remove_brick_to_world(b, 'add')

#Move all to the bottom
for b in bricks:
    while can_go_lower(b):
        b = move_lower(b)

result = 0

#Check the ones that are safe to disintegrate
for b in bricks:
    add_remove_brick_to_world(b, 'remove')
    if sum(can_go_lower(x) for x in bricks if x[2] >= b[2] and x[2] <= b[5] + 1) == 0:
        result += 1
    add_remove_brick_to_world(b, 'add')

print(result)
            


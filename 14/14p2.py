import numpy as np
import time

start = time.time()

with open('input.txt') as file:
    temp = [list(line.strip()) for line in file]

platform = np.array(temp)

def move_one_rock(y, x, dir):
    if platform[y, x] != 'O':
        raise ValueError('there is no rock here')

    if dir in 'NS':
        j = y
        if dir == 'N':
            while j > 0 and platform[j - 1, x] == '.' :
                j -= 1

        if dir == 'S':
            while j + 1 <= h - 1 and platform[j + 1, x] == '.':
                j += 1

        if j != y:
            platform[j, x] = 'O'
            platform[y, x] = '.'

    elif dir in 'WE':
        i = x
        if dir == 'W':
            while i > 0 and platform[y, i - 1] == '.' :
                i -= 1

        if dir == 'E':
            while i + 1 <= w - 1 and platform[y, i + 1] == '.' :
                i += 1

        if i != x:
            platform[y, i] = 'O'
            platform[y, x] = '.'

    else:
        raise ValueError('dir must be one of N S W E')


def move_all(dir):
    if dir == 'N':
        for i in range(h):
            for j in range(w):
                if platform[i, j] == 'O':
                    move_one_rock(i, j, dir)

    elif dir == 'S':
        for i in range(h-1, -1, -1):
            for j in range(w):
                if platform[i, j] == 'O':
                    move_one_rock(i, j, dir)

    elif dir == 'W':
        for j in range(w):
            for i in range(h):
                if platform[i, j] == 'O':
                    move_one_rock(i, j, dir)

    elif dir == 'E':
        for j in range(w-1, -1, -1):
            for i in range(h):
                if platform[i, j] == 'O':
                    move_one_rock(i, j, dir)

    else:
        raise ValueError('dir must be one of N S W E')


def cycle():
    move_all('N')
    move_all('W')
    move_all('S')
    move_all('E')


def load():
    result = 0
    for i in range(h):
        for j in range(w):
            if platform[i][j] == 'O':
                result += h - i
    return result


h, w = platform.shape
loads = np.array([], dtype='int32')
last20 = np.zeros(20, dtype='int32')
cl = 0  # cycle length

for i in range(200):
    cycle()
    l = load()
    loads = np.append(loads, l)
    last20 = np.append(last20[1:], l)
    print(i, l)
    #print(loads)
    #print(last20)
    if np.all(np.in1d(last20, loads[:-20])):
        break


for i in range(1, 100):
    if np.array_equal(loads[-2*i:], np.roll(loads[-2*i:], i)):
        print('The cycle length is: ', i)
        cl = i
        break

print(loads[(loads.shape[0] // cl - 1) * cl + 999999999 % cl])
print(time.time() - start)

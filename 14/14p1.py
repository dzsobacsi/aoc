with open('input.txt') as file:
    platform = [list(line.strip()) for line in file]

def move_one_rock(y, x):
    if platform[y][x] != 'O':
        raise ValueError('there is no rock here')

    j = y
    while platform[j - 1][x] == '.' and j > 0:
        j -= 1

    if j != y:
        platform[j][x] = 'O'
        platform[y][x] = '.'


h = len(platform)
w = len(platform[0])
result = 0

for i in range(h):
    for j in range(w):
        if platform[i][j] == 'O':
            move_one_rock(i, j)

for i in range(h):
    for j in range(w):
        if platform[i][j] == 'O':
            result += h - i

print(result)

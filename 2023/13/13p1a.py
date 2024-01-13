import numpy as np

patterns = []
result = 0

with open('input.txt') as file:
    new_pattern = []
    for i, line in enumerate(file):
        if line == '\n':
            patterns.append(np.array(new_pattern))
            new_pattern = []
        else:
            new_pattern.append(list(line.strip()))
    patterns.append(np.array(new_pattern))


def solver(patt):
    h, w = patt.shape

    #Check vertical axes
    for i in range(1, w):
        hw = min(i, w - i)
        slice = patt[:, i - hw : i + hw]
        if np.array_equal(slice, np.flip(slice, 1)):
            return i

    #Check horizontal axes
    for j in range(1, h):
        hh = min(j, h - j)
        slice = patt[j - hh : j + hh, :]
        if np.array_equal(slice, np.flip(slice, 0)):
            return 100 * j

    return 0


for patt in patterns:
    result += solver(patt)

print(result)

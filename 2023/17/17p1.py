import numpy as np

tmp = []
with open('small.txt') as file:
    for line in file:
        tmp.append([int(x) for x in list(line.strip())])

map = np.array(tmp)

print(map)
print(map.shape)
print(map.dtype)

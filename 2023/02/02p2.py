import numpy as np

result = 0

with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        cubesets = line.split(':')[1].split(';')
        minimum_set = {}
        for cs in cubesets:
            colors_l = [s.strip() for s in cs.split(',')]
            print(i+1, colors_l)
            colors_d = {}
            for c in colors_l:
                num_color = c.split()
                colors_d[num_color[1]] = int(num_color[0])
            for k, v in colors_d.items():
                minimum_set[k] = max(minimum_set.get(k, 0), v)
        print(minimum_set)
        result += np.prod(list(minimum_set.values()))

print(result)

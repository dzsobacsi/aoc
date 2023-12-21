seeds = []
map3d = []
map = []

with open('input.txt', 'r') as file:
    seeds = [int(x) for x in file.readline().split(':')[1].strip().split()]
    for line in file:
        if line[0].isalpha():
            continue
        if line[0].isnumeric():
            map.append([int(x) for x in line.strip().split()])
        else:
            if len(map):
                map3d.append(map)
                map = []
    if len(map):
        map3d.append(map)
        del map


def convert_all(map3d, x, i=0):
    def convert(map, x):
        for row in map:
            if x in range(row[1], row[1] + row[2]):
                return row[0] + x - row[1]
        return x

    if i == len(map3d):
        return x
    else:
        result = convert(map3d[i], x)
        return convert_all(map3d, result, i+1)


result = min(convert_all(map3d, x) for x in seeds)
print(result)

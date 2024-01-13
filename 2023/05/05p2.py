seeds = []
ranges = []
map3d = []
map = []

with open('input.txt') as file:
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


def convert_num(map, x):
    for row in map:
        if x in range(row[1], row[1] + row[2]):
            return row[0] + x - row[1]
    return x


def convert_rng(map, rng):
    """
    receives a map and a range
    returns a list of ranges
    """
    map_ranges = []
    for _, st, ln in map:
        map_ranges.append(range(st, st+ln))
    map_ranges.sort(key=lambda x: x.start)
    if map_ranges[0].start > 0:
        map_ranges.insert(0, range(0, map_ranges[0].start))
    map_ranges.append(range(map_ranges[-1].stop, int(1e20)))

    result = []
    for r in map_ranges:
        if rng.start < r.stop and rng.stop > r.start:  # there is any kind of overlap
            start = rng.start if rng.start in r else r.start
            stop = rng.stop if rng.stop in r else r.stop
            result.append(range(start, stop))
    if len(result) == 0:
        result.append(rng)
    result = [range(convert_num(map, r.start), convert_num(map, r.stop - 1) + 1) for r in result]
    return result


def convert_all(map3d, rng):
    ls_rng = [rng]
    for map in map3d:
        ls_rng = [item for row in [convert_rng(map, r) for r in ls_rng] for item in row]
    return ls_rng


for i in range(0, len(seeds), 2):
    ranges.append(range(seeds[i], seeds[i] + seeds[i+1]))

result = [item for row in [convert_all(map3d, r) for r in ranges] for item in row]
result.sort(key=lambda x: x.start)

print(result[0].start)

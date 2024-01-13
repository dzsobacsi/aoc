instructions = []
nodes = {}

with open('input.txt') as file:
    instructions = list(file.readline().strip())
    _ = file.readline()
    for line in file:
        k = line.split('=')[0].strip()
        v1, v2 = line.split('=')[1].split(',')
        v1 = v1.strip().strip('(')
        v2 = v2.strip().strip(')')
        nodes[k] = (v1, v2)


def is_good_as_final(l):
    return all(x.endswith('Z') for x in l)


curr = [x for x in nodes.keys() if x.endswith('A')]
result = 0
instructions = [0 if x == 'L' else 1 for x in instructions]

while not is_good_as_final(curr):
    to = instructions[result % len(instructions)]
    curr = [nodes[x][to] for x in curr]
    print(curr)
    result += 1
    if result % 1000000 == 0:
        print(result)

print(result)

from math import lcm
import time

start_time = time.time()
instructions = []
nodes = {}

with open('input.txt') as file:
    instructions = list(file.readline().strip())
    file.readline()
    for line in file:
        k = line.split('=')[0].strip()
        v1, v2 = line.split('=')[1].split(',')
        v1 = v1.strip().strip('(')
        v2 = v2.strip().strip(')')
        nodes[k] = (v1, v2)

curr = [x for x in nodes.keys() if x.endswith('A')]
results = []
instructions = [0 if x == 'L' else 1 for x in instructions]

for i in curr:
    result = 0
    c = i
    while not c.endswith('Z'):
        to = instructions[result % len(instructions)]
        c = nodes[c][to]
        result += 1
    results.append(result)

print(lcm(*results))
print(time.time() - start_time)

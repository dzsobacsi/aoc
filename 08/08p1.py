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

curr = 'AAA'
result = 0
instructions = [0 if x == 'L' else 1 for x in instructions]

while curr != 'ZZZ':
    to = instructions[result % len(instructions)]
    curr = nodes[curr][to]
    result += 1

print(result)

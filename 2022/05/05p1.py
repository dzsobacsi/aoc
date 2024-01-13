import numpy as np

crates = []
instructions = []

with open('input.txt', 'r') as file:
    for line in file:
        if line.strip().endswith(']'):
            row = []
            for i, ch in enumerate(line.strip('\n')):
                if i % 4 == 1:
                    row.append(ch)
            crates.append(row)
        if line.startswith('move'):
            instructions.append(line.strip())

places = np.empty(10, dtype='object')
for i in range(10):
    places[i] = []

for row in reversed(crates):
    for i, crate in enumerate(row):
        if crate != ' ':
            places[i + 1].append(crate)

for row in instructions:
    instr = row.split()
    for _ in range(int(instr[1])):
        places[int(instr[5])].append(places[int(instr[3])].pop())

for i in range(1, 10):
    print(places[i][-1], end='')

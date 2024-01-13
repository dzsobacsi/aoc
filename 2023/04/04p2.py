import numpy as np
import time

start_time = time.time()
input = []

with open('input.txt', 'r') as file:
    for line in file:
        input.append(line.strip())

counts = np.ones(len(input), dtype='int32')

for i, row in enumerate(input):
    a, b = row.split(':')[1].split('|')
    winners = set(int(x) for x in a.strip().split())
    ownnums = set(int(x) for x in b.strip().split())
    matches = len(winners.intersection(ownnums))
    for j in range(1, matches + 1):
        counts[i + j] += counts[i]

print(np.sum(counts))
print(time.time() - start_time)

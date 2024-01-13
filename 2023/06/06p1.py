from math import sqrt, floor, ceil

times = []
distances = []
result = 1

with open('input.txt', 'r') as file:
    times     = [int(x) for x in file.readline().split(':')[1].strip().split()]
    distances = [int(x) for x in file.readline().split(':')[1].strip().split()]

def nr_of_ways(T, s):
    res1 = (T - sqrt(T**2 - 4*s)) / 2
    res2 = (T + sqrt(T**2 - 4*s)) / 2

    res1 = res1 + 1 if res1.is_integer() else res1
    res2 = res2 - 1 if res2.is_integer() else res2

    return floor(res2) - ceil(res1) + 1

for t, s in zip(times, distances):
    result *= nr_of_ways(t, s)

print(result)

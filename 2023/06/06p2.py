from math import sqrt, floor, ceil

time = 0
distance = 0

with open('input.txt', 'r') as file:
    time     = int(file.readline().split(':')[1].strip().replace(' ', ''))
    distance = int(file.readline().split(':')[1].strip().replace(' ', ''))

def nr_of_ways(T, s):
    res1 = (T - sqrt(T**2 - 4*s)) / 2
    res2 = (T + sqrt(T**2 - 4*s)) / 2

    res1 = res1 + 1 if res1.is_integer() else res1
    res2 = res2 - 1 if res2.is_integer() else res2

    return floor(res2) - ceil(res1) + 1

result = nr_of_ways(time, distance)
print(result)

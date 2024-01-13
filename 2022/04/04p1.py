result = 0

length = lambda x: x[1] - x[0] + 1

with open('input.txt', 'r') as file:
    for line in file:
        a, b = line.strip().split(',')
        a = [int(x) for x in a.strip().split('-')]
        b = [int(x) for x in b.strip().split('-')]
        # b is going to be the shorter
        if length(a) < length(b):
            a, b = b, a
        if b[0] >= a[0] and b[1] <= a[1]:
            result += 1

print(result)

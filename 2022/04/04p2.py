result = 0

with open('input.txt', 'r') as file:
    for line in file:
        a, b = line.strip().split(',')
        a = [int(x) for x in a.strip().split('-')]
        b = [int(x) for x in b.strip().split('-')]
        # b is going to be on the right
        if b[1] < a[1]:
            a, b = b, a
        if b[0] <= a[1]:
            result += 1

print(result)

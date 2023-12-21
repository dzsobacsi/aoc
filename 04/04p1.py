result = 0

with open('input.txt', 'r') as file:
    for line in file:
        a, b = line.split(':')[1].split('|')
        winners = set(int(x) for x in a.strip().split())
        ownnums = set(int(x) for x in b.strip().split())
        matches = len(winners.intersection(ownnums))
        result += 2 ** (matches - 1) if matches else 0

print(result)

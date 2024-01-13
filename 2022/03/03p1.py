result = 0

def get_priority(ch):
    return ord(ch) - 38 if ch.isupper() else ord(ch) - 96

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        n = len(line) // 2
        a = set(line[:n])
        b = set(line[n:])
        result += get_priority(a.intersection(b).pop())

print(result)

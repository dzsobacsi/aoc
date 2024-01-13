with open('input.txt') as file:
    line = file.readline().strip()

steps = [s.strip() for s in line.split(',')]

def hash(s):
    result = 0
    for ch in s:
        result += ord(ch)
        result *= 17
        result %= 256
    return result

print(sum(hash(s) for s in steps))

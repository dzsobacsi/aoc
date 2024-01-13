result = 0
input = []

def get_priority(ch):
    return ord(ch) - 38 if ch.isupper() else ord(ch) - 96

with open('input.txt', 'r') as file:
    for line in file:
        input.append(line.strip())

for i in range(len(input) // 3):
    result += get_priority(
        set(input[3 * i])\
            .intersection(set(input[3 * i + 1]))\
            .intersection(set(input[3 * i + 2]))\
            .pop()
    )

print(result)

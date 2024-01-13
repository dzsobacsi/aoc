result = 0
subtotal = 0

with open('input.txt', 'r') as file:
    for line in file:
        if line.strip():
            subtotal += int(line.strip())
        else:
            result = max(result, subtotal)
            subtotal = 0

print(result)

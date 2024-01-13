calories = []
subtotal = 0

with open('input.txt', 'r') as file:
    for line in file:
        if line.strip():
            subtotal += int(line.strip())
        else:
            calories.append(subtotal)
            subtotal = 0

calories.sort(reverse=True)

print(sum(calories[:3]))

import re

stars = []    # a list of tuples with the star indices
input = []    # a list of string just like the input file
numbers = []  # a list of tuples like: (number, row-nr, start-position, end-position(excl.))
result = 0

# filling up input
with open('input.txt', 'r') as file:
    for line in file:
        input.append(line.strip())

# filling up numbers
for i, row in enumerate(input):
    res = re.finditer('\d+', row)
    for j in res:
        numbers.append((int(j.group()), i, *j.span()))

# filling up stars
for i, row in enumerate(input):
    matches = re.finditer('\*', row)
    for m in matches:
        stars.append((i, m.start()))

def gear_ratio(nums, star):
    """
    receives a list of numbers as tuples
    receives a star as a tuple
    returns the gear ratio if the star is a gear and zero otherwise
    """
    gear_ratio = 1
    neighbors = 0
    for n in nums:
        if star[0] in range(n[1] - 1, n[1] + 2) \
            and star[1] in range(n[2] - 1, n[3] + 1):
                gear_ratio *= n[0]
                neighbors += 1

    return gear_ratio if neighbors == 2 else 0

for s in stars:
    result += gear_ratio(numbers, s)

print(result)

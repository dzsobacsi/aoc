import numpy as np
import re

input = []    # a list of string just like the input file
temp_mtx = []
numbers = []  # a list of tuples like: (number, row-nr, start-position, end-position(excl.))
result = 0

# filling up input
with open('input.txt', 'r') as file:
    for line in file:
        input.append(line.strip())
        temp_mtx.append(list(line.strip()))

# creating a numpy array with all the characters
char_np = np.array(temp_mtx)

# filling up numbers
for i, row in enumerate(input):
    res = re.finditer('\d+', row)
    for j in res:
        numbers.append((int(j.group()), i, *j.span()))


def is_part_number(arr, num):
    """
    receives a numpy array containing the input
    and a number as tuple: (number, row-nr, start-position, end-position(excl.))
    returns the number itself if the number is a part number and zero otherwise
    """
    row_start = max(num[1] - 1, 0)
    row_end = min(num[1] + 2, arr.shape[0])
    col_start = max(num[2] - 1, 0)
    col_end = min(num[3] + 1, arr.shape[1])

    not_num = ~np.char.isnumeric(arr[row_start:row_end, col_start:col_end])
    not_dot = arr[row_start:row_end, col_start:col_end] != '.'

    return num[0] if np.any(np.logical_and(not_num, not_dot)) else 0

for i in numbers:
    result += is_part_number(char_np, i)

print(result)

import numpy as np

patterns = []
result = 0

with open('input.txt') as file:
    new_pattern = []
    for i, line in enumerate(file):
        if line == '\n':
            patterns.append(np.array(new_pattern))
            new_pattern = []
        else:
            new_pattern.append(list(line.strip()))
    patterns.append(np.array(new_pattern))

def find_identical_columns(patt):
    """
    Returns a list of column indices when column i and i+1 are identical
    with each other
    Returns an empty list if no adjacent identical columns are found
    """
    result = []
    for i in range(patt.shape[1] - 1):
        if np.array_equal(patt[:, i], patt[:, i+1]):
            result.append(i)
    return result

def find_identical_rows(patt):
    """
    Returns a list of row indices when row i and i+1 are identical
    with each other
    Returns an empty list if no adjacent identical rows are found
    """
    result = []
    for i in range(patt.shape[0] - 1):
        if np.array_equal(patt[i, :], patt[i+1, :]):
            result.append(i)
    return result

def is_mirror_col(patt, k):
    n = min(k + 1, patt.shape[1] - k - 1)
    for i in range(n):
        if not np.array_equal(patt[:, k - i], patt[:, k + 1 + i]):
            return 0
    return k + 1

def is_mirror_row(patt, k):
    n = min(k + 1, patt.shape[0] - k - 1)
    for i in range(n):
        if not np.array_equal(patt[k - i, :], patt[k + 1 + i, :]):
            return 0
    return 100 * (k + 1)

for i, patt in enumerate(patterns):
    cols = find_identical_columns(patt)
    rows = find_identical_rows(patt)
    if len(cols):
        for c in cols:
            res = is_mirror_col(patt, c)
            if res:
                print(i, 'column', c, res)
                result += res
    if len(rows):
        for r in rows:
            res = is_mirror_row(patt, r)
            if res:
                print(i, 'row', r, res)
                result += res


print(result)

"""
k = 0
print(find_identical_columns(patterns[k]))
print(find_identical_rows(patterns[k]))
#print(is_mirror_col(patterns[k], find_identical_columns(patterns[k])[0]))
#print(is_mirror_row(patterns[k], find_identical_rows(patterns[k])[1]))
print(patterns[k])
print(patterns[k].shape)
#"""

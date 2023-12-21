result = 0

def next(l):
    result = []
    for i in range(1, len(l)):
        result.append(l[i] - l[i-1])
    return result

def predict(l):
    if sum(l) == 0:
        return 0
    return predict(next(l)) + l[-1]

with open('input.txt') as file:
    for line in file:
        result += predict([int(x) for x in line.strip().split()])

print(result)

splits = {
    'x': [],
    'm': [],
    'a': [],
    's': []
}

with open('small.txt') as file:
    for line in file:
        if line[0].isalpha():
            name, rest = line.split('{')
            rules = rest[:-2].split(',')
            for r in rules:
                if ':' in r:
                    cond = r.split(':')[0]
                    splits[cond[0]].append(cond[2:])


print(splits)

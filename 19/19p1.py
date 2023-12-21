parts = []
wfs = {}

with open('input.txt') as file:
    for line in file:
        if line[0].isalpha():
            name, rest = line.split('{')
            rules = rest[:-2].split(',')
            wfs[name] = rules
        elif line.startswith('{'):
            part = {}
            for i in line[1: -2].split(','):
                cat, value = i.split('=')
                part[cat] = int(value)
            parts.append(part)

def sum_rating(part):
    return sum(part.values())

def is_good(part, wf):
    for i in wfs[wf]:
        if ':' in i:
            cond, target = i.split(':')
            if eval(f'part["{cond[0]}"]{cond[1:]}'):  # cond is like 's>1234'
                next = target
            else:
                continue
        else:
            next = i

        if next in 'AR':
            return True if next == 'A' else False
        else:
            return is_good(part, next)

print(sum(sum_rating(p) for p in parts if is_good(p, 'in')))

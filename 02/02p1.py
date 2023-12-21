possibleones = []

def is_possible(cubes):
    return cubes.get('red', 0) <= 12 \
        and cubes.get('green', 0) <= 13 \
        and cubes.get('blue', 0) <= 14

with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        cubesets = line.split(':')[1].split(';')
        game_possible = True
        for cs in cubesets:
            colors_l = [s.strip() for s in cs.split(',')]
            print(i+1, colors_l)
            colors_d = {}
            for c in colors_l:
                num_color = c.split()
                colors_d[num_color[1]] = int(num_color[0])
            if not is_possible(colors_d):
                game_possible = False
                break
        print(game_possible)
        if game_possible:
            possibleones.append(i+1)

print(sum(possibleones))

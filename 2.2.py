
f = open('Input2', 'r')

total = 0

for line in f.readlines():
    cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    line = line.rstrip()
    gameId = int(line[5:line.index(':')])

    for group in line.split(';'):
        for key in cubes.keys():
            if key in group:
                if int(group[group.index(key)-3:group.index(key)]) > cubes[key]:
                    cubes[key] = int(group[group.index(key)-3:group.index(key)])

    total += (cubes['red']*cubes['green']*cubes['blue'])

print(total)

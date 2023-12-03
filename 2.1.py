
f = open('Input2', 'r')
cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

total = 0

for line in f.readlines():
    line = line.rstrip()
    possible = True
    gameId = int(line[5:line.index(':')])

    for group in line.split(';'):
        for key in cubes.keys():
            if key in group:
                if int(group[group.index(key)-3:group.index(key)]) > cubes[key]:
                    possible = False
                    break

    if possible:
        total += gameId

print(total)
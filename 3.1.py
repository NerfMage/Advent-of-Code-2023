
f = open('Input3', 'r')

schematic = []

for line in f.readlines():
    schematic.append(line.rstrip())

for line in schematic:
    for character in line:
        if not character.isnumeric() and character != '.':
            lineNum = schematic.index(line)
            index = line.index(character)
            surrounding = [
                schematic[lineNum+1][index-3:index+3],
                schematic[lineNum][index-4:index+4],
                schematic[lineNum-1][index-3:index+3],
            ]

        else:
            pass


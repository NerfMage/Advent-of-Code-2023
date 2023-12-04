
f = open('Input1', 'r')

total = 0

for line in f.readlines():
    line = line.rstrip()

    pointer = 0
    while not line[pointer].isnumeric():
        pointer += 1
    first = line[pointer]

    pointer = len(line) - 1
    while not line[pointer].isnumeric():
        pointer -= 1
    last = line[pointer]

    total += int(first+last)

print(total)

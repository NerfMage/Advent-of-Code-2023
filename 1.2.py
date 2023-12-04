
f = open('Input1', 'r')

total = 0
digits = [str(i) for i in range(1, 10)] + ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in f.readlines():
    line = line.rstrip()

    pointer = 0
    while not any(digit in line[:pointer] for digit in digits):
        pointer += 1

    for digit in digits:
        if digit in line[:pointer]:
            first = digits.index(digit) % 9 + 1

    pointer = len(line) - 1
    while not any(digit in line[pointer:] for digit in digits):
        pointer -= 1

    for digit in digits:
        if digit in line[pointer:]:
            last = digits.index(digit) % 9 + 1

    total += (10*first) + last

print(total)

from itertools import groupby


def look_and_say(line):
    sequence = groupby(line)
    return "".join(f"{sum(1 for _ in i)}{char}" for char, i in sequence)


line = "1"
for _ in range(30):
    (line := look_and_say(line))

print(len(line))

from itertools import groupby

def look_and_say(s):
    return "".join(f"{len(list(x))}{n}" for n, x in groupby(s))

sequence='1'
for _ in range(30):
    sequence=look_and_say(sequence)
print(len(sequence))
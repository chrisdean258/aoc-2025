#!/usr/bin/env python3

ipt = open(0).read().splitlines()

start = ipt[0].index("S")

beams = set((start,))

s = 0
for line in ipt[1:]:
    splitters = set(i for i, c in enumerate(line) if c == "^")
    splits = splitters & beams
    beams -= splits
    s += len(splits)
    for split in splits:
        beams.add(split - 1)
        beams.add(split + 1)
print(s)

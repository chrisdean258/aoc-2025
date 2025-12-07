#!/usr/bin/env python3

from collections import defaultdict

ipt = open(0).read().splitlines()

start = ipt[0].index("S")

beams = defaultdict(int)
beams[start] = 1

s = 0
for line in ipt[1:]:
    splits = set(i for i, c in enumerate(line) if c == "^")
    for split in splits:
        if split in beams:
            v = beams.pop(split)
            beams[split - 1] += v
            beams[split + 1] += v
print(sum(beams.values()))

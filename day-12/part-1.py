#!/usr/bin/env python3

import math

s = 0
for line in open(0).read().split("\n\n")[-1].splitlines():
    dims, _, counts = line.partition(": ")
    size = math.prod(int(a) for a in dims.split("x"))
    s += size >= 9 * sum(int(a) for a in counts.split())

print(s)

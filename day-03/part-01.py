#!/usr/bin/env python3

lines = open(0).read().splitlines()

s = 0
for line in lines:
    m = max(line[:-1])
    mindex = line.index(m)
    mm = max(line[mindex + 1:])
    s += int(m + mm)
print(s)

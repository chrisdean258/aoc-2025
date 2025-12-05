#!/usr/bin/env python3

import sys
from collections import deque

ranges = []
for line in sys.stdin:
    if not line.strip():
        break
    ranges.append([int(i) for i in line.split("-")])

ranges.sort()


i = len(ranges) - 1

while i > 0:
    hl, hh = ranges[i]
    ll, lh = ranges[i - 1]
    if hl > lh:
        i -= 1
        continue

    l = min(hl, ll)
    h = max(hh, lh)

    ranges[i - 1: i + 1] = [[l, h]]
    i -= 1

s = 0
for l, h in ranges:
    s += h - l + 1

print(s)

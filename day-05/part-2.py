#!/usr/bin/env python3

import sys

ranges = []
for line in sys.stdin:
    if not line.strip():
        break
    ranges.append([int(i) for i in line.split("-")])

ranges.sort()

q = ranges[1:]
ranges = ranges[:1]

for hl, hh in q:
    ll, lh = ranges[-1]

    if hl > lh:
        ranges.append((hl, hh))
    else:
        ranges.pop()
        ranges.append((ll, max(lh, hh)))

s = 0
for low, high in ranges:
    s += high - low + 1
print(s)

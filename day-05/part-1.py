#!/usr/bin/env python3

import sys

ranges = []
for line in sys.stdin:
    if not line.strip():
        break
    ranges.append([int(i) for i in line.split("-")])

nums = [int(i.strip()) for i in sys.stdin]

s = 0
for num in nums:
    for low, high in ranges:
        if low <= num <= high:
            s += 1
            break
print(s)


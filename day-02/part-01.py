#!/usr/bin/env python3
import math

ids = open(0).read().strip().split(",")
ids = [[int(i) for i in id.split("-")] for id in ids]


def valid(start, stop):
    l0 = math.floor(math.log10(start))
    if l0 < math.floor(math.log10(stop)):
        return valid(start, 10 ** (l0 + 1) - 1) + valid(10 ** (l0 + 1), stop)
    if l0 % 2 == 0:  # for odd number of digits
        return []

    s = str(start)
    first = int(s[:len(s)//2])

    s = str(stop)
    last = int(s[:len(s)//2])

    rv = []
    for i in range(first, last + 1):
        v = i * 10 ** ((l0 + 1) // 2) + i
        if start <= v <= stop:
            rv.append(v)

    return rv


s = 0
for id in ids:
    v = valid(*id)
    s += sum(v)
print(s)

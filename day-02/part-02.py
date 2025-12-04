#!/usr/bin/env python3
import math

# flake8: noqa

ids = open(0).read().strip().split(",")
ids = [[int(i) for i in id.split("-")] for id in ids]


def valid_(start, stop, base):
    l0 = math.floor(math.log10(start))
    if l0 < math.floor(math.log10(stop)):
        return valid_(start, 10 ** (l0 + 1) - 1, base) + valid_(10 ** (l0 + 1), stop, base)
    if (l0 + 1) % base != 0:  # for odd number of digits
        return []

    s = str(start)
    first = int(s[:len(s)//base])

    s = str(stop)
    last = int(s[:len(s)//base])

    rv = []
    for i in range(first, last + 1):
        v = int(str(i) * base)
        if start <= v <= stop:
            rv.append(v)

    return rv


def valid(start, stop):
    s = set()
    for i in range(2, len(str(stop)) + 1):
        v = valid_(start, stop, i)
        s |= set(v)
    return s


s = 0
for id in ids:
    v = valid(*id)
    s += sum(v)
print(s)

#!/usr/bin/env python3

lines = open(0).read().splitlines()


def maximize(line, num):
    if num == 1:
        return max(line)
    m = max(line[:-num + 1])
    ll = line[line.index(m) + 1:]
    return m + maximize(ll, num - 1)


s = 0
for line in lines:
    v = maximize(line, 12)
    s += int(v)
print(s)

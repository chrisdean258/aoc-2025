#!/usr/bin/env python3

s = 50
t = 0
for line in open(0):
    if line[0] == "L":
        s += int(line[1:])
    else:
        s -= int(line[1:])
    if s %100 == 0:
        t += 1
print(t)

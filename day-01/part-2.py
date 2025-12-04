#!/usr/bin/env python3


s = 50
t = 0
prev_0 = False
for line in open(0):
    num = int(line[1:])
    t += num // 100
    num = num % 100
    if line[0] == "L":
        s -= int(num)
    else:
        s += int(num)
    if prev_0:
        prev_0 = False
    elif s <= 0 or s >= 100:
        t += 1
    s = s % 100
    if s == 0:
        prev_0 = True
print(t)

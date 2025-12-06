#!/usr/bin/env python3
import math

ipt = [line.split() for line in open(0)]

ops = ipt[-1]
nums = zip(*[[int(a) for a in line] for line in ipt[:-1]])

s = 0
for op, line in zip(ops, nums):
    if op == "+":
        s += sum(line)
    else:
        s += math.prod(line)
print(s)

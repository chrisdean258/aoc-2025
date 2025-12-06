#!/usr/bin/env python3
import math

ipt = open(0).read().splitlines()


ops = ipt[-1].split()

nums = ["".join(s) for s in zip(*ipt[:-1])]

s = 0
i = 0
tmp = []
for num in nums + [""]:
    if not num.strip():
        if ops[i] == "+":
            s += sum(tmp)
        else:
            s += math.prod(tmp)
        i += 1
        tmp = []
    else:
        tmp.append(int(num.strip()))
print(s)

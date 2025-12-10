#!/usr/bin/env python3

from z3 import Int, Optimize, sat

# flake8: noqa


def solve(target, buttons):
    opt = Optimize()
    vs = [Int('x' + str(i)) for i in range(len(buttons))]
    exprs = [0] * len(target)
    for v, button in zip(vs, buttons):
        for b in button:
            exprs[b] += v
    for v in vs:
        opt.add(v >= 0)
    for expr, t in zip(exprs, target):
        opt.add(expr == t)
    obj = opt.minimize(sum(vs))
    result = opt.check()
    return obj.value().as_long()
    if result == sat:
        model = opt.model()
        v = sum(model[v] for v in vs)
        breakpoint()
        return v


s = 0
for line in open(0):
    lights, *rest = line.split()
    buttons = [[int(i) for i in button[1:-1].split(",")]
               for button in rest[:-1]]
    target = [int(v) for v in rest[-1][1:-1].split(",")]
    s += solve(target, buttons)
print(s)

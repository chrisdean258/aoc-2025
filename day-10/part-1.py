#!/usr/bin/env python3

from functools import reduce
from collections import deque


def bfs(target, buttons):
    seen = set()
    q = deque([(0, 0)])
    while q:
        count, item = q.popleft()
        if item == target:
            return count
        for button in buttons:
            v = item ^ button
            if v not in seen:
                q.append((count + 1, v))
                seen.add(v)
    raise Exception((target, buttons))


s = 0
for line in open(0):
    lights, *rest = line.split()
    lights = lights[1:-1]
    lights = reduce(lambda a, b: a | b, (1 << i for i,
                    c in enumerate(lights) if c == "#"))
    buttons = [
        reduce(lambda a, b: a | b,   (1 << int(i)
               for i in button[1:-1].split(",")))
        for button in rest[:-1]]
    s += bfs(lights, buttons)
print(s)

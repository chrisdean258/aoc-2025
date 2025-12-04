#!/usr/bin/env python3

from collections import defaultdict

grid = open(0).read().splitlines()

lines = len(grid)
cols = len(grid[0])

gg = defaultdict(int)

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "@":
            gg.setdefault((i, j), 0)
            gg[(i-1, j-1)] += 1
            gg[(i-1, j+0)] += 1
            gg[(i-1, j+1)] += 1

            gg[(i+1, j-1)] += 1
            gg[(i+1, j+0)] += 1
            gg[(i+1, j+1)] += 1

            gg[(i, j-1)] += 1
            gg[(i, j+1)] += 1

s = set()
for (i, j), v in gg.items():
    if v < 4 and 0 <= i < lines and 0 <= j < cols and grid[i][j] == "@":
        s.add((i, j))

print(len(s))

rmed = set()
while s:
    i, j = s.pop()
    rmed.add((i, j))
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            if (ii, jj) != (0, 0):
                ti = i + ii
                tj = j + jj
                t = (ti, tj)
                gg[t] -= 1
                if gg[t] < 4 and t not in rmed and 0 <= ti < lines and 0 <= tj < cols and grid[ti][tj] == "@":
                    s.add(t)

print(len(rmed))

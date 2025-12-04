#!/usr/bin/env python3

from collections import defaultdict

grid = open(0).read().splitlines()

lines = len(grid)
cols = len(grid[0])


def valid(i, j):
    return 0 <= i < lines and 0 <= j < cols and grid[i][j] == "@"


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

s = 0
for (i, j), v in sorted(gg.items()):
    if v < 4 and valid(i, j):
        s += 1
print(s)

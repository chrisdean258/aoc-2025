#!/usr/bin/env python3

tls = [[int(a) for a in line.split(",")] for line in open(0)]
m = 0
tiles = set()
r_lookup = {}
c_lookup = {}

rs = sorted(list(set(t[0] for t in tls)))
cs = sorted(list(set(t[1] for t in tls)))

prev = -1
for i, r in enumerate(rs):
    if abs(r - prev) == 1:
        raise Exception("BAD")
    r_lookup[r] = i * 2
    prev = r

prev = -1
for i, c in enumerate(cs):
    if abs(c - prev) == 1:
        raise Exception("BAD")
    c_lookup[c] = i * 2
    prev = c

tiles = [(r_lookup[r], c_lookup[c]) for r, c in tls]


def tile_of(a):
    r1, c1 = a
    r1 = rs[r1 // 2]
    c1 = cs[c1 // 2]
    return r1, c1


all_tiles = set()

for (r1, c1), (r2, c2) in zip(tiles, tiles[1:] + [tiles[0]]):
    if r1 == r2:
        for c in range(min(c1, c2), max(c1, c2) + 1):
            all_tiles.add((r1, c))
    else:
        for r in range(min(r1, r2), max(r1, r2) + 1):
            all_tiles.add((r, c1))

r, c = tiles[0]
testers = [(r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1), ]

for r, c in testers:
    num = sum(((i, c) in all_tiles) for i in range(r))
    if num % 2 == 1:
        start = r, c
        break

all_tiles.add(start)
q = [start]
while q:
    r, c = q.pop()
    for i in range(-1, 2):
        for j in range(-1, 2):
            t = (r + i, c + j)
            if t not in all_tiles:
                all_tiles.add(t)
                q.append(t)


def area(a, b):
    r1, c1 = tile_of(a)
    r2, c2 = tile_of(b)
    return (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)


def good(a, b):
    r1, c1 = a
    r2, c2 = b
    for r in range(min(r1, r2) + 1, max(r1, r2), 2):
        if (r, c1) not in all_tiles or (r, c2) not in all_tiles:
            return False
    for c in range(min(c1, c2) + 1, max(c1, c2), 2):
        if (r1, c) not in all_tiles or (r2, c) not in all_tiles:
            return False
    return True


m = 0
for i, tile in enumerate(tiles):
    for other in tiles[i + 1:]:
        a = area(tile, other)
        if a <= m:
            continue
        if good(tile, other):
            m = a
print(m)

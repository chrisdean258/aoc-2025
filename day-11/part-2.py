#!/usr/bin/env python3

from functools import cache

graph = {}

for line in open(0):
    key, _, edges = line.partition(": ")
    graph[key] = edges.split()


@cache
def all_paths(start, end):
    if start == end:
        return 1
    s = 0
    for node in graph.get(start, []):
        s += all_paths(node, end)
    return s


dac2out = all_paths("dac", "out")
fft2dac = all_paths("fft", "dac")
svr2fft = all_paths("svr", "fft")
print(dac2out * fft2dac * svr2fft)

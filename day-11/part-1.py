#!/usr/bin/env python3

graph = {}

for line in open(0):
    key, _, edges = line.partition(": ")
    graph[key] = edges.split()


def all_paths(graph, start, end):
    if start == end:
        return 1
    s = 0
    for node in graph[start]:
        s += all_paths(graph, node, end)
    return s


print(all_paths(graph, "you", "out"))

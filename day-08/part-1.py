#!/usr/bin/env python3

from collections import Counter
import math


class Node:
    def __init__(self, xyz):
        self.x, self.y, self.z = xyz
        self.edges = []
        self.label = None

    def add_edge(self, other):
        self.edges.append(other)
        other.edges.append(self)

    def dist_sq(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2  # noqa:E501

    def dfs(self, label):
        if self.label is not None:
            return self.label
        self.label = label
        for node in self.edges:
            node.dfs(label)

    def __str__(self):
        return f"{self.pt()}"

    def __repr__(self):
        return f"{self.pt()}"

    def pt(self):
        return (self.x, self.y, self.z)


nodes = [
    Node([int(a) for a in line.split(",")])
    for line in open(0)]

dists = []

for n1 in nodes:
    for n2 in nodes:
        if n1.pt() < n2.pt():
            dists.append((n1.dist_sq(n2), n1, n2))

dists.sort(key=lambda a: a[0])


for d2, n1, n2 in dists[:1000]:
    n1.add_edge(n2)


for i, node in enumerate(nodes):
    node.dfs(i)

componenets = Counter((node.label for node in nodes))
print(math.prod(c[1] for c in componenets.most_common(3)))

#!/usr/bin/env python3


class Node:
    def __init__(self, i, xyz):
        self.x, self.y, self.z = xyz
        self.label = i
        self.parent = self

    def dist_sq(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2  # noqa:E501

    def union(self, other):
        s_r = self.root()
        o_r = other.root()

        if s_r.label == o_r.label:
            return s_r.label
        if s_r.label < o_r.label:
            o_r.label = s_r.label
            o_r.parent = s_r
            return s_r.label
        return other.union(self)

    def pt(self):
        return (self.x, self.y, self.z)

    def root(self):
        root = self
        while root.parent != root:
            root = root.parent
        return root

    def find(self):
        root = self.root()

        node = self
        while node.parent != root:
            node.label = root.label
            t, node = node, node.parent
            t.parent = root
        return root.label


nodes = [
    Node(i, [int(a) for a in line.split(",")])
    for i, line in enumerate(open(0))]

dists = []

for n1 in nodes:
    for n2 in nodes:
        if n1.pt() < n2.pt():
            dists.append((n1.dist_sq(n2), n1, n2))

dists.sort(key=lambda a: a[0])

for _, n1, n2 in dists:
    label = n1.union(n2)
    if label == 0:
        for node in nodes:
            if node.find() != 0:
                break
        else:
            print(n1.x *  n2.x)
            break

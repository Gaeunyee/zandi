import sys
from heapq import *
from functools import total_ordering
input = sys.stdin.readline


def decode(t, l):
    global res
    if t.isLeaf:
        res += l * t.size
    for n in t.child:
        decode(n, l + 1)


class Node:
    def __init__(self, size, leaf):
        self.isLeaf = leaf
        self.size = size
        self.child = []

    def append(self, node):
        self.size += node.size
        self.child.append(node)

    def __eq__(self, other):
        return self.size == other.size

    def __lt__(self, other):
        return self.size < other.size


def solve():
    N, K = map(int, input().split())
    d = 0 if (N-1) % (K-1) == 0 else K - 1 - (N-1) % (K-1)
    lst = list(map(lambda x: Node(int(x), True), input().split()))
    for _ in range(d):
        lst.append(Node(0, True))
    heapify(lst)
    while len(lst) > 1:
        c = 0
        t = Node(0, False)
        while lst and c < K:
            c += 1
            t.append(heappop(lst))
        heappush(lst, t)
    return lst[0]


T = int(input().strip())
for _ in range(T):
    top = solve()
    res = 0
    decode(top, 0)
    print(res)

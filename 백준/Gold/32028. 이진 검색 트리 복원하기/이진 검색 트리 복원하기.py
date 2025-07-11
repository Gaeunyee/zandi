import sys
from collections import deque
from functools import total_ordering
input = sys.stdin.readline

N = int(input().strip())
lst = [[] for i in range(N+1)]
nodes = []

class Node:
    def __init__(self, num, depth, idx):
        self.num = num
        self.depth = depth
        self.left, self.right = -1, -1
        self.idx = idx
        self.l, self.r = -(2*10**9 + 1), 2*10**9 + 1

    def __eq__(self, other):
        return self.num == other.num

    def __lt__(self, other):
        return self.num < other.num

for i in range(N):
    a, h = map(int, input().split())
    nodes.append(Node(a, h, i+1))
    lst[h].append(nodes[i])

f = 1
for i in range(1, N):
    if len(lst[i]) > (1 << (i-1)):
        f = 0
        break
    lst[i+1].sort()
    lower = 0
    for j in lst[i]:
        if lower >= len(lst[i+1]):
            break
        if j.l <= lst[i+1][lower].num < j.num:
            j.left = lst[i+1][lower].idx
            lst[i + 1][lower].l, lst[i+1][lower].r = j.l, j.num-1
            lower += 1
        if lower >= len(lst[i+1]):
            break
        if j.num < lst[i+1][lower].num <= j.r:
            j.right = lst[i + 1][lower].idx
            lst[i + 1][lower].l, lst[i + 1][lower].r = j.num+1, j.r
            lower += 1
    if lower != len(lst[i+1]):
        f = 0
        break




if f:
    for n in nodes:
        print(n.left, n.right)
else:
    print(-1)


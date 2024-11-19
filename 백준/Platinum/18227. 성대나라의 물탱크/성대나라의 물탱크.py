import sys
from math import ceil, log
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, C = map(int, input().split())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2 - 1
graph = [[] for _ in range(N+1)]
e_in = [-1]*(N+1)
e_out = [-1]*(N+1)
depth = [-1]*(N+1)
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
cnt = 0


def ett(tmp, d):
    global cnt
    cnt += 1
    e_in[tmp] = cnt
    depth[tmp] = d + 1
    for next in graph[tmp]:
        if e_in[next] == -1:
            ett(next, d+1)
    e_out[tmp] = cnt
ett(C, 0)


def editTree(i, new):
    while i != 0:
        tree[i] += new
        i //= 2


def getSum(start, end):
    res = 0
    while start <= end:
        if start % 2 == 1:
            res += tree[start]
            start += 1
        if end % 2 == 0:
            res += tree[end]
            end -= 1
        start, end = start//2, end//2
    return res


Q = int(input().strip())

for _ in range(Q):
    cmd, x = map(int, input().split())
    if cmd == 1:
        i = e_in[x]
        editTree(startIndex + i, 1)
    else:
        s, t = e_in[x], e_out[x]
        print(getSum(startIndex+s, startIndex+t)*depth[x])


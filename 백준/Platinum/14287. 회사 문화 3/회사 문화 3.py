import sys
from math import ceil, log
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2 - 1
graph = [[] for _ in range(N+1)]
e_in = [-1]*(N+1)
e_out = [-1]*(N+1)
lst = [0]+list(map(int, input().split()))
for i in range(2, N+1):
    graph[lst[i]].append(i)
cnt = 0


def ett(tmp):
    global cnt
    cnt += 1
    e_in[tmp] = cnt
    for next in graph[tmp]:
        if e_in[next] == -1:
            ett(next)
    e_out[tmp] = cnt
ett(1)


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


for _ in range(Q):
    cmd, *x = map(int, input().split())
    if cmd == 1:
        i = e_in[x[0]]
        editTree(startIndex + i, x[1])
    else:
        s, t = e_in[x[0]], e_out[x[0]]
        print(getSum(startIndex+s, startIndex+t))


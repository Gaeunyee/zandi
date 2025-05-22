import sys
from collections import deque
from heapq import *
from math import sqrt
input = sys.stdin.readline

INF = 10**9

def solve():
    def find(a):
        if par[a] == a:
            return a
        par[a] = find(par[a])
        return par[a]

    def union(a, b):
        x, y = find(a), find(b)
        if x == y:
            return 0
        if x > y:
            x, y = y, x
        par[y] = x
        return 1

    N = int(input().strip())
    par = [i for i in range(N+1)]
    point = []
    for _ in range(N):
        point.append(tuple(map(float, input().split())))
    dist = []
    for i in range(N):
        for j in range(i+1, N):
            dist.append((sqrt((point[i][0]-point[j][0])**2 + (point[i][1]-point[j][1])**2), i, j))

    dist.sort()
    cnt = 0
    res = 0
    for d, a, b in dist:
        if cnt >= N-1:
            break
        if union(a, b):
            cnt += 1
            res += d

    print(res)


solve()

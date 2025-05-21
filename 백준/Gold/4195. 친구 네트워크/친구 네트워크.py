import sys
from collections import deque
from heapq import *
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
            return size[x]
        if x > y:
            x, y = y, x
        par[y] = x
        size[x] += size[y]
        return size[x]

    F = int(input().strip())
    dic = {}
    par = [i for i in range(F*2 + 1)]
    size = [1]*(F*2 + 1)
    for _ in range(F):
        a, b = input().split()
        if a not in dic:
            dic[a] = len(dic)
        if b not in dic:
            dic[b] = len(dic)
        print(union(dic[a], dic[b]))


T = int(input().strip())
for _ in range(T):
    solve()



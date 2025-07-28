import sys
from heapq import *
input = sys.stdin.readline


N, K = map(int, input().split())
graph = [[] for _ in range(N)]
edge = []
for _ in range(K):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))


edge.sort()
par = [i for i in range(N)]

def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def union(a, b):
    x, y = find(a), find(b)
    if x == y:
        return False
    if x > y:
        x, y = y, x
    par[x]= y
    return True

cnt = 0
cost = 0
for c, a, b in edge:
    if cnt == N-1:
        break
    if union(a, b):
        cnt += 1
        cost += c
        graph[a].append((b, c))
        graph[b].append((a, c))

visited = [0]*N
def dfs(x, d):
    visited[x] = 1
    m = d
    e = x
    for i, c in graph[x]:
        if not visited[i]:
            visited[i] = 1
            t, te = dfs(i, d+c)
            if m < t:
                e = te
                m = t
    return m, e

d, x = dfs(0, 0)
visited = [0]*N
print(cost)
print(dfs(x, 0)[0])

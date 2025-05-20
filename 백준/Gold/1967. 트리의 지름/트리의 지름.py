import sys
sys.setrecursionlimit(10**5)
from collections import deque
from heapq import *
input = sys.stdin.readline

INF = 10**9

def dfs(t, d):
    visited[t] = d
    m, v = -1, -1
    for n, c in graph[t]:
        if not visited[n]:
            k, e = dfs(n, c+d)
            if k > m:
                m, v = k, e
    if m == -1:
        return d, t
    return m, v

N = int(input().strip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [0]*(N+1)
w, s = dfs(1, 1)
visited = [0]*(N+1)
w, e = dfs(s, 1)
print(w-1)

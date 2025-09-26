import sys
from collections import deque
input = sys.stdin.readline
INF = 10**9

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
g = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    if g[u][v] == INF:
        graph[u].append(v)
        g[u][v] = 1
for i in range(1, N+1):
    g[i][i] = 0

f = 1
def dfs(t):
    global f
    visited[t] = 1
    for i in graph[t]:
        if visited[i] == 1:
            f = 0
            return
        elif visited[i] == 0:
            dfs(i)
    visited[t] = -1

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
    if not f:
        print(-1)
        exit()

cnt = [0]*(N+1)
inv_cnt = [0]*(N+1)
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if g[i][j] > g[i][k]+g[k][j]:
                g[i][j] = g[i][k]+g[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if g[i][j] != INF:
            cnt[j] += 1
            inv_cnt[i] += 1

for i in range(1, N+1):
    print(cnt[i], N-inv_cnt[i]+1)


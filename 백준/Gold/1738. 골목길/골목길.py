import sys
from collections import deque
input = sys.stdin.readline
INF = (1<<64)-1

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, -w))


parent = [INF] * (N+1)
dist = [INF] * (N+1)
inQ = [0] * (N+1)
dist[1] = 0
qu = deque()
qu.append(1)
isQ = [False] * (N+1)
isQ[1] = True
inQ[1] = 1
while qu:
    node = qu.popleft()
    isQ[node] = False
    if inQ[node] >= N+1:
        continue
    for next, cost in graph[node]:
        if dist[next] > dist[node] + cost:
            dist[next] = dist[node] + cost
            parent[next] = node
            if not isQ[next] and inQ[next] < N:
                qu.append(next)
                inQ[next] += 1
                isQ[next] = True

visited = [False]*(N+1)
for i in range(1, N+1):
    if inQ[i] >= N and not visited[i]:
        visited[i] = True
        qu = deque([i])
        while qu:
            t = qu.popleft()
            visited[t] = True
            for next, cost in graph[t]:
                if not visited[next]:
                    qu.append(next)
if visited[N]:
    print(-1)

else:
    tr = N
    path = []
    while tr != INF:
        path.append(tr)
        tr = parent[tr]
    print(*(reversed(path)))


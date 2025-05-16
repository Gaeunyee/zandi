import sys
from collections import deque
input = sys.stdin.readline
INF = (1<<64)-1

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


dist = [INF] * (N+1)
inQ = [0] * (N+1)
dist[1] = 0
qu = deque()
qu.append(1)
isQ = [False] * (N+1)
isQ[1] = True
inQ[1] = 1
flag = 1
while qu:
    node = qu.popleft()
    isQ[node] = False
    if inQ[node] >= N:
        flag = 0
        break
    for next, cost in graph[node]:
        if dist[next] > dist[node] + cost:
            dist[next] = dist[node] + cost
            if not isQ[next] and inQ[next] < N:
                qu.append(next)
                inQ[next] += 1
                isQ[next] = True


if not flag:
    print(-1)

else:
    for i in dist[2:]:
        print(i if i != INF else -1)
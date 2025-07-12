import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

qu = deque([1])
wb = [0, 1, 0]
visited = [0]*(N+1)
visited[1] = 1
f = 1
while qu:
    t = qu.popleft()
    for n in graph[t]:
        if visited[n] == visited[t] and visited[n]:
            f = 0
            break
        if not visited[n]:
            visited[n] = visited[t] * -1
            wb[visited[t] * -1] += 1
            qu.append(n)

print(wb[1]*wb[-1]*2 if f else 0)


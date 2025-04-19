import sys
from collections import deque
input = sys.stdin.readline


N, M, R = map(int, input().split())
visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    counter = 1
    qu = deque()
    qu.append(start)
    visited[start] = 1
    while qu:
        tmp = qu.popleft()
        for nxt in sorted(graph[tmp]):
            if not visited[nxt]:
                counter += 1
                visited[nxt] = counter
                qu.append(nxt)

    for i in visited[1:]:
        print(i)

bfs(R)




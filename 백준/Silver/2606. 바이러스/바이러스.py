import sys
from collections import deque
input = sys.stdin.readline


N = int(input().strip())
E = int(input().strip())

visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(E):
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
        for nxt in sorted(graph[tmp], reverse=True):
            if not visited[nxt]:
                counter += 1
                visited[nxt] = counter
                qu.append(nxt)

    print(counter-1)

bfs(1)




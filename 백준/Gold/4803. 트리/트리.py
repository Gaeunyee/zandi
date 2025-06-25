import sys
from collections import deque
input = sys.stdin.readline

dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(s):
    qu = deque()
    qu.append(s)
    visited[s] = 1
    counter = 1
    deg = 0
    while qu:
        t = qu.popleft()
        for n in graph[t]:
            deg += 1
            if not visited[n]:
                visited[n] = 1
                counter += 1
                qu.append(n)

    return 1 if (counter-1)*2 == deg else 0


tem = ['No trees.', 'There is one tree.', 'A forest of T trees.']
c = 0
while True:
    c += 1
    N, M = map(int, input().split())
    if N == M == 0:
        break
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0]*(N+1)
    res = 0
    for x in range(1, N+1):
        if not visited[x]:
            res += bfs(x)
    print(f'Case {c}:', f'{tem[res]}' if res < 2 else f'A forest of {res} trees.')



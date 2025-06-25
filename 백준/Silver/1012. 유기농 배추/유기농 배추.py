import sys
from collections import deque
input = sys.stdin.readline

dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(x, y):
    qu = deque()
    qu.append((x, y))
    visited[x][y] = 1
    while qu:
        tx, ty = qu.popleft()
        for dx, dy in dxdy:
            nx, ny = tx+dx, ty+dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                qu.append((nx, ny))

    return 1

T = int(input().strip())


for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[0] * (M + 1) for _ in range(N + 1)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    visited = [[0] * (M + 1) for _ in range(N + 1)]
    res = 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1 and not visited[x][y]:
                res += bfs(x, y)
    print(res)



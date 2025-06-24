import sys
from collections import deque
input = sys.stdin.readline

dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(input().strip())
graph = []
for _ in range(N):
    graph.append(input().strip())

visited = [[0]*(N+1) for _ in range(N+1)]


def bfs(x, y):
    counter = 1
    qu = deque()
    qu.append((x, y))
    visited[x][y] = 1
    while qu:
        tx, ty = qu.popleft()
        for dx, dy in dxdy:
            nx, ny = tx+dx, ty+dy
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == '1' and not visited[nx][ny]:
                counter += 1
                visited[nx][ny] = 1
                qu.append((nx, ny))

    return counter


res = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == '1' and not visited[x][y]:
            res.append(bfs(x, y))

res.sort()
print(len(res))
for i in res:
    print(i)




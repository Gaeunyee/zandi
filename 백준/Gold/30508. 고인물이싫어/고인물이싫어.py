import sys
from collections import deque
input = sys.stdin.readline
INF = 10**9

dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
h, w = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

qu = deque()
ok = [[0]*(M+1) for _ in range(N+1)]  # ok = 1, not ok = -1
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    qu.append((x-1, y-1))
    ok[x-1][y-1] = 1

while qu:
    x, y = qu.popleft()
    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            if graph[x][y] <= graph[nx][ny] and ok[nx][ny] == 0:
                ok[nx][ny] = 1
                qu.append((nx, ny))
for i in range(N):
    for j in range(1, M):
        ok[i][j] += ok[i][j-1]

s = 0
res = 0

for j in range(M-w+1):
    s = 0
    for i in range(h):
        s += ok[i][j+w-1] - ok[i][j-1]
    if s == h * w:
        res += 1
    for i in range(1, N-h+1):
        s -= ok[i-1][j+w-1] - ok[i-1][j-1]
        s += ok[i+h-1][j+w-1] - ok[i+h-1][j-1]
        if s == h*w:
            res += 1
print(res)



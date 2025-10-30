import sys
from collections import deque
input = sys.stdin.readline

dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
g1, g2 = [], []
for _ in range(N):
    g1.append(list(map(int, input().split())))
for _ in range(N):
    g2.append(list(map(int, input().split())))

visited = [[0]*M for _ in range(N)]

def bfs(u, v, c1, c2):
    qu = deque()
    qu.append((u, v))
    while qu:
        tx, ty = qu.popleft()
        if g2[tx][ty] != c2:
            return False
        for dx, dy in dxdy:
            nx, ny = tx+dx, ty+dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if g1[nx][ny] == c1:
                        visited[nx][ny] = 1
                        qu.append((nx, ny))

    return True
f = 0
r = 1
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = 1
            if g1[i][j] != g2[i][j]:
                f += 1
            if not bfs(i, j, g1[i][j], g2[i][j]):
                r = 0
                break

print('YES' if r and f <= 1 else 'NO')



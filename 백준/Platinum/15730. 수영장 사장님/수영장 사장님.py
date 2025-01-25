import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
height = []
for _ in range(N):
    height.append(list(map(int, input().split())))

res = 0

def fill(i, j):
    global res
    h = height[i][j]

    for u, v in dxdy:
        sx, sy = i+u, j+v
        if 0 <= sx < N and 0 <= sy < M and height[sx][sy] < h:
            buffer = [(sx, sy)]
            visited = [[0] * M for _ in range(N)]
            visited[sx][sy] = 1
            qu = deque()
            qu.append((sx, sy))
            ok = True
            while qu:
                if not ok:
                    break
                tx, ty = qu.popleft()
                if tx == 0 or tx == N-1 or ty == 0 or ty == M-1:
                    if height[tx][ty] < h:
                        ok = False
                        break
                for dx, dy in dxdy:
                    nx, ny = tx+dx, ty+dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if tx == 0 or tx == N - 1 or ty == 0 or ty == M - 1:
                            if height[tx][ty] < h:
                                ok = False
                                break
                        if height[nx][ny] < h and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            qu.append((nx, ny))
                            buffer.append((nx, ny))
            if ok:
                for x, y in buffer:
                    res += h - height[x][y]
                    height[x][y] = h

for i in range(N):
    for j in range(M):
        fill(i, j)
print(res)

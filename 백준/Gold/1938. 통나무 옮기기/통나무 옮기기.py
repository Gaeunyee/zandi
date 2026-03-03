import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
matrix = [[1]*(N+2) for _ in range(N+2)]
start = (0, 0, 0) # 0이 가로, 1이 세로
end = (0, 0, 0)
for i in range(1, N+1):
    l = input().strip()
    for j in range(1, N+1):
        if l[j-1] != '1':
            matrix[i][j] = 0
        if l[j-1] == 'B' and start == (0, 0, 0):
            if j != N and l[j] == 'B':
                start = (i, j+1, 0)
            else:
                start = (i+1, j, 1)
        if l[j-1] == 'E' and end == (0, 0, 0):
            if j != N and l[j] == 'E':
                end = (i, j+1, 0)
            else:
                end = (i+1, j, 1)

qu = deque([start])
visited = [[[0, 0] for _ in range(N+2)] for _ in range(N+2)]
visited[start[0]][start[1]][start[2]] = 1
res = -1
while qu:
    # u, d, l, r, t
    tx, ty, td = qu.popleft()
    if (tx, ty, td) == end:
        res = visited[tx][ty][td]
        break
    if td == 0: # 가로
        for k in (1, -1):
            f = 1
            for i in range(-1, 2):
                if matrix[tx+k][ty-i] == 1:
                    f = 0
                    break
            if f and not visited[tx+k][ty][td]:
                visited[tx + k][ty][td] = visited[tx][ty][td] + 1
                qu.append((tx+k, ty, td))

            f = 1
            for i in range(-1, 2):
                if matrix[tx][ty-i+k] == 1:
                    f = 0
                    break
            if f and not visited[tx][ty+k][td]:
                visited[tx][ty+k][td] = visited[tx][ty][td] + 1
                qu.append((tx, ty+k, td))
        f = 1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if matrix[tx+i][ty+j] == 1:
                    f = 0
                    break
        if f and not visited[tx][ty][1]:
            qu.append((tx, ty, 1))
            visited[tx][ty][1] = visited[tx][ty][0] + 1
    else:
        for k in (1, -1):
            f = 1
            for i in range(-1, 2):
                if matrix[tx-i][ty+k] == 1:
                    f = 0
                    break
            if f and not visited[tx][ty+k][td]:
                visited[tx][ty + k][td] = visited[tx][ty][td] + 1
                qu.append((tx, ty+k, td))

            f = 1
            for i in range(-1, 2):
                if matrix[tx - i+k][ty] == 1:
                    f = 0
                    break
            if f and not visited[tx+k][ty][td]:
                visited[tx+k][ty][td] = visited[tx][ty][td] + 1
                qu.append((tx+k, ty, td))
        f = 1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if matrix[tx + i][ty + j] == 1:
                    f = 0
                    break
        if f and not visited[tx][ty][0]:
            qu.append((tx, ty, 0))
            visited[tx][ty][0] = visited[tx][ty][1] + 1

print(res-1 if res != -1 else 0)






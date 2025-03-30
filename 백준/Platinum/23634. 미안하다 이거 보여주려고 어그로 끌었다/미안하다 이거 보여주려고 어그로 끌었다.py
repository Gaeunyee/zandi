import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
visited = [[-1]*(C) for _ in range(R)]
par = [[(i, j) for j in range(C)] for i in range(R)]
graph = []

def find(a):
    x, y = a
    if par[x][y] == (x, y):
        return a
    par[x][y] = find(par[x][y])
    return par[x][y]


def union(a, b, t):
    global ct, size, res
    x1, y1 = find(a)
    x2, y2 = find(b)
    if (x1, y1) != (x2, y2):
        if x1 < x2:
            par[x1][y1] = (x2, y2)
        else:
            par[x2][y2] = (x1, y1)
        if graph[x1][y1] == '0' and graph[x2][y2] == '0':
            ct = t
            res = size
        return True
    return False


cnt = 0
ct = 0
size = 0
time = 0
res = 0

def solve():
    global cnt, ct, size, time, res
    qu = deque()
    for i in range(R):
        line = input().strip()
        graph.append(list(line))
        for j in range(C):
            if line[j] == '0':
                qu.append((i, j, 0))
                cnt += 1
                visited[i][j] = 0
        size = cnt
        res = size

    while qu:
        tx, ty, t = qu.popleft()
        if t > time:
            time = t
            size = cnt
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = tx+dx, ty+dy
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '1' and visited[nx][ny] == -1:
                    cnt += 1
                    graph[nx][ny] = '0'
                    visited[nx][ny] = t+1
                    par[nx][ny] = (tx, ty)
                    qu.append((nx, ny, t+1))
                if ((graph[nx][ny] == '0')
                        and visited[nx][ny] <= visited[tx][ty]):
                    union((tx, ty), (nx, ny), t)
    print(ct, res)


solve()

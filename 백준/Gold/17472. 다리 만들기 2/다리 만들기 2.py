import sys
from collections import deque
input = sys.stdin.readline

INF = 10**9

dxdy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
I = 0

def find(a):
    if par[a] == a:
        return a
    par[a] = find(par[a])
    return par[a]


def union(a, b):
    x, y = find(a), find(b)
    if x == y:
        return 0
    if x > y:
        x, y = y, x
    par[y] = x
    return 1


def bfs():
    global I

    for i in range(N):
        for j in range(M):
            if id[i][j] or not graph[i][j]:
                continue
            qu = deque()
            qu.append((i, j))
            I += 1
            id[i][j] = I
            while qu:
                x, y = qu.popleft()
                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny]:
                        if not id[nx][ny]:
                            id[nx][ny] = id[x][y]
                            qu.append((nx, ny))




N, M = map(int, input().split())
par = [i for i in range(7)]
id = [[0]*M for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
bfs()
edge = []
def makeEdge(x, y):
    for dx, dy in dxdy:
        tx, ty = x+dx, y+dy
        l = 0
        while 0 <= tx < N and 0 <= ty < M and not graph[tx][ty]:
            l += 1
            tx, ty = tx + dx, ty + dy
        if l >= 2 and 0 <= tx < N and 0 <= ty < M and graph[tx][ty]:
            edge.append((l, id[x][y], id[tx][ty]))


for i in range(N):
    for j in range(M):
        if id[i][j]:
            makeEdge(i, j)

edge.sort()
cnt, res = 0, 0
for d, a, b in edge:
    if cnt >= I-1:
        break
    if union(a, b):
        cnt += 1
        res += d

print(res if cnt == I-1 else -1)

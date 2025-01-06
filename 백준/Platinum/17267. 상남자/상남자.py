import sys
from collections import deque
input = sys.stdin.readline
INF = (1<<64)-1

N, M = map(int, input().split())
L, R = map(int, input().split())
graph = []
qu = deque()
for i in range(N):
    l = list(input().strip())
    for j in range(M):
        if l[j] == '2':
            start = (i, j)
            qu.append((i, j, L, R))
    graph.append(l)
visited = [[False]*M for _ in range(N)]
visited[start[0]][start[1]] = True
cnt = 0
while qu:
    tx, ty, l, r = qu.popleft()
    cnt += 1
    i = 1
    while tx+i < N and graph[tx+i][ty] != '1' and not visited[tx+i][ty]:
        qu.append((tx+i, ty, l, r))
        visited[tx+i][ty] = True
        i += 1
    i = -1
    while tx + i >= 0 and graph[tx+i][ty] != '1' and not visited[tx+i][ty]:
        qu.append((tx+i, ty, l, r))
        visited[tx + i][ty] = True
        i -= 1
    if r and ty+1 < M and graph[tx][ty+1] != '1' and not visited[tx][ty+1]:
        qu.append((tx, ty+1, l, r-1))
        visited[tx][ty+1] = True
    if l and ty-1 >= 0 and graph[tx][ty-1] != '1' and not visited[tx][ty-1]:
        qu.append((tx, ty-1, l-1, r))
        visited[tx][ty-1] = True

print(cnt)


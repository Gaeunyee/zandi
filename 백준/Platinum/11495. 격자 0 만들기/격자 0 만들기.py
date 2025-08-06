import sys
from collections import deque
input = sys.stdin.readline

dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
INF = 10**5
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    size = N*M + 3
    src = N*M + 1
    graph = [[] for _ in range(size)]
    capacity = [dict() for _ in range(size)]
    flow = [dict() for _ in range(size)]
    grid = []
    s = 0
    for _ in range(N):
        t = list(map(int, input().split()))
        s += sum(t)
        grid.append(t)

    for i in range(N):
        for j in range(M):
            if i%2 != j%2:
                graph[M * i + j].append(src)
                graph[src].append(M*i + j)
                capacity[src][M * i + j] = grid[i][j]
                capacity[M * i + j][src] = 0
                flow[M * i + j][src] = 0
                flow[src][M * i + j] = 0
                for dx, dy in dxdy:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < N and 0 <= ny < M:
                        graph[M * i + j].append(M * nx + ny)
                        graph[M * nx + ny].append(M * i + j)
                        capacity[M * i + j][M*nx + ny] = INF
                        capacity[M * nx + ny][M * i + j] = 0
                        flow[M * i + j][M * nx + ny] = 0
                        flow[M * nx + ny][M*i + j] = 0
            else:
                graph[M * i + j].append(-1)
                graph[-1].append(M*i + j)
                capacity[M*i + j][-1] = grid[i][j]
                capacity[-1][M * i + j] = 0
                flow[M * i + j][-1] = 0
                flow[-1][M * i + j] = 0

    while True:
        qu = deque()
        qu.append(src)
        par = [-2] * size
        fl = 10 ** 6
        while qu and par[-1] == -2:
            tmp = qu.popleft()
            for next in graph[tmp]:
                if capacity[tmp][next] - flow[tmp][next] > 0 and par[next] == -2:
                    par[next] = tmp
                    qu.append(next)

        if par[-1] == -2:
            break
        end = -1
        while end != src:
            fl = min(fl, capacity[par[end]][end] - flow[par[end]][end])
            end = par[end]
        end = -1
        while end != src:
            flow[par[end]][end] += fl
            flow[end][par[end]] -= fl
            end = par[end]

    for i in range(N):
        for j in range(M):
            if i%2 != j%2:
                s -= flow[src][M*i + j]
    print(s)

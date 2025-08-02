import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
size = N*N + 2*N + 5
src = N*N + 2*N
graph = [[] for _ in range(size)]
capacity = [dict() for _ in range(size)]
flow = [dict() for _ in range(size)]

M = 0
right = list(map(int, input().split()))
M += sum(right)
for i in range(N*N, N*N + N):
    capacity[src][i] = right[i-N*N]
    capacity[i][src] = 0
    flow[src][i] = 0
    flow[i][src] = 1
    graph[i].append(src)
    graph[src].append(i)

bottom = list(map(int, input().split()))
for i in range(N * N + N, N * N + 2*N):
    capacity[i][-1] = bottom[i - (N * N + N)]
    capacity[-1][i] = 0
    flow[i][-1] = 0
    flow[-1][i] = 0
    graph[i].append(-1)
    graph[-1].append(i)



l, r = -1, 10001
for i in range(N):
    for j in range(N):
        graph[N * i + j].append(N * N + i)
        graph[N * i + j].append(N * N + N + j)
        graph[N*N + i].append(N*i + j)
        graph[N*N + N + j].append(N*i + j)

        flow[N * i + j][N * N + i] = 0
        flow[N * i + j][N * N + N + j] = 0
        flow[N * N + i][N * i + j] = 0
        flow[N * N + N + j][N * i + j] = 0

while l+1 < r:
    for i in flow:
        for k in i.keys():
            i[k] = 0
    m = (l+r) // 2
    for i in range(N):
        for j in range(N):
            capacity[N * N + i][N * i + j] = m
            capacity[N * i + j][N * N + N + j] = m
            capacity[N * i + j][N * N + i] = 0
            capacity[N * N + N + j][N * i + j] = 0


    while True:
        qu = deque()
        qu.append(src)
        par = [-2]*size
        fl = 10**6
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

    res = 0
    for i in range(N*N, N*N+N):
        res += flow[src][i]
    if res == M:
        r = m
    else:
        l = m


print(r)

for i in flow:
    for k in i.keys():
        i[k] = 0
m = r
for i in range(N * N):
    capacity[src][i] = m
for i in range(N):
    for j in range(N):
        capacity[N * N + i][N * i + j] = m
        capacity[N * i + j][N * N + N + j] = m

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
    for j in range(N):
        print(flow[N*N+i][N*i + j], end= ' ')
    print()

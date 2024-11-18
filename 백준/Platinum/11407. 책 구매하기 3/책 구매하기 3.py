import sys
from collections import deque

input = sys.stdin.readline
SIZE = 110
INF = 10 ** 6

N, M = map(int, input().split())
capacity = [[0] * SIZE*2 for _ in range(SIZE*2)]
flow = [[0] * SIZE*2 for _ in range(SIZE*2)]
costs = [[0] * SIZE*2 for _ in range(SIZE*2)]

graph = [[] for _ in range(SIZE * 2)]
w = list(map(int, input().split()))
for i in range(1, N+1):
    graph[0].append((i, 0))
    capacity[0][i] = w[i-1]
    costs[0][i] = 0

w = list(map(int, input().split()))
for j in range(1, M+1):
    graph[N+j].append((-1, 0))
    capacity[N+j][-1] = w[j-1]
    costs[N+j][-1] = 0

for i in range(1, M+1):
    line = list(map(int, input().split()))
    for j in range(1, N+1):
        capacity[j][N+i] = line[j-1]

for i in range(1, M+1):
    line = list(map(int, input().split()))
    for j in range(1, N+1):
        graph[j].append((N+i, line[j-1]))
        graph[N+i].append((j, -line[j-1]))
        costs[j][N+i] = line[j-1]
        costs[N+i][j] = -line[j-1]

res, cnt = 0, 0
while True:
    parent = [-2] * (SIZE * 2 + 2)
    dist = [INF] * (SIZE * 2)
    dist[0] = 0
    qu = deque()
    qu.append(0)
    isQ = [False] * (SIZE * 2 + 2)
    isQ[0] = True
    while qu:
        node = qu.popleft()
        isQ[node] = False
        for next, cost in graph[node]:
            if (capacity[node][next] - flow[node][next] > 0
                    and dist[next] > dist[node] + cost):
                dist[next] = dist[node] + cost
                parent[next] = node
                if not isQ[next]:
                    qu.append(next)
                    isQ[next] = True

    if parent[-1] == -2:
        break
    i = -1
    fl = INF

    while i != 0:
        fl = min(fl, capacity[parent[i]][i] - flow[parent[i]][i])
        i = parent[i]
    cnt += fl
    i = -1
    while i != 0:
        flow[parent[i]][i] += fl
        flow[i][parent[i]] -= fl
        i = parent[i]
        res += costs[parent[i]][i] * fl
print(cnt)
print(res)

import sys
from collections import deque

input = sys.stdin.readline
SIZE = 21
INF = 10 ** 6

N = int(input().strip())
capacity = [[1] * SIZE*2 for _ in range(SIZE*2)]
flow = [[0] * SIZE*2 for _ in range(SIZE*2)]
costs = [[0] * SIZE*2 for _ in range(SIZE*2)]

graph = [[] for _ in range(SIZE * 2)]
for i in range(1, N+1):
    arg = list(map(int, input().split()))
    graph[0].append((i, 0))
    costs[0][i] = 0
    for nxt in range(1, N+1):
        cost = arg[nxt-1]
        graph[i].append((N + nxt, cost))
        graph[N + nxt].append((i, -cost))
        costs[i][N+nxt], costs[N+nxt][i] = cost, -cost
        capacity[N+nxt][i] = 0

for j in range(1, N+1):
    graph[N+j].append((-1, 0))
    costs[N+j][-1] = 0
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
    cnt += 1
    while i != 0:
        flow[parent[i]][i] += 1
        flow[i][parent[i]] -= 1
        i = parent[i]
        res += costs[parent[i]][i]
print(res)

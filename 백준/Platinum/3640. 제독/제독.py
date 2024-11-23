import sys
from collections import deque

input = sys.stdin.readline
SIZE = 1100
INF = 10 ** 6
while True:
    inp = input()
    if inp == '':
        break
    N, E = map(int, inp.split())
    capacity = [[0] * SIZE*2 for _ in range(SIZE*2)]
    flow = [[0] * SIZE*2 for _ in range(SIZE*2)]
    costs = [[0] * SIZE*2 for _ in range(SIZE*2)]

    graph = [[] for _ in range(SIZE * 2)]
    for i in range(1, N):
        graph[-i].append((i, 0))
        graph[i].append((-i, 0))
        capacity[-i][i] = 1

    for i in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((-b, c))
        costs[a][-b] = c
        capacity[a][-b] = 1
        graph[-b].append((a, -c))
        costs[-b][a] = -c

    graph[0].append((1, 0))
    capacity[0][1] = 2
    res, cnt = 0, 0
    while True:
        parent = [INF] * (SIZE * 2 + 2)
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

        if parent[-N] == INF:
            break

        i = -N
        while i != 0:
            flow[parent[i]][i] += 1
            flow[i][parent[i]] -= 1
            res += costs[parent[i]][i]
            i = parent[i]


    print(res)

import sys

input = sys.stdin.readline
SIZE = 120
mid = 55
INF = 10 ** 6
N, M = map(int, input().split())
capacity = [[0]*SIZE for _ in range(SIZE)]
flow = [[0]*SIZE for _ in range(SIZE)]
graph = [[] for _ in range(SIZE)]
graph[0] = [i for i in range(N, 0, -1)]  # 소스
for i in range(1, N+1):
    for j in range(mid+M, mid, -1):
        graph[i].append(j)
        capacity[i][j] = 1
for j in range(mid+M, mid, -1):  # 1 start index
    graph[j].append(-1)  # 싱크: -1
    for i in range(N, 0, -1):
        graph[j].append(i)

cmd = [-1]+list(map(int, input().split()))
for i in range(1, N+1):
    capacity[0][i] = cmd[i]

cmd = [-1] + list(map(int, input().split()))
for i in range(1, M+1):
    capacity[mid+i][-1] = cmd[i]
capacity_o = capacity[:]

def dfs(node, cf):
    vi[node] = True
    if node == -1:
        return cf
    for next in graph[node]:
        if (capacity[node][next] - flow[node][next] > 0 and (not vi[next])):
            res = dfs(next, min(cf, capacity[node][next] - flow[node][next]))
            if res:
                flow[node][next] += res
                flow[next][node] -= res
                return res
    return 0

def isOk(node, cf, start, end):
    vi[node] = True
    if node == start:
        res = isOk(end, min(cf, capacity[node][end] - flow[node][end]), start, end)
        if res:
            flow[node][end] += res
            flow[end][node] -= res
        return res

    for next in graph[node]:
        if (capacity[node][next] - flow[node][next] > 0 and (not vi[next] or next == start)):
            if next == start:
                flow[node][next] += cf
                flow[next][node] -= cf
                return cf

            res = isOk(next, min(cf, capacity[node][next] - flow[node][next]), start, end)
            if res:
                flow[node][next] += res
                flow[next][node] -= res
                return res
    return 0

flag = 1
while True:
    parent = [INF] * SIZE
    vi = [False] * SIZE
    capacity = capacity_o[:]

    if not dfs(0, INF):
        break



for i in range(1, N+1):
    if capacity[0][i] - flow[0][i] != 0:
        flag = 0
for i in range(mid+1, M+mid+1):
    if capacity[i][-1] - flow[i][-1] != 0:
        flag = 0


for i in range(1, N+1):
    for j in range(mid+1, mid+M+1):
        if flow[i][j]:
            vi = [False] * SIZE
            if isOk(j, INF, j, i):
                capacity[i][j] = 0
        else:
            capacity[i][j] = 0

res = []
for i in range(1, N+1):
    matrix = ""
    for next in graph[i]:
        matrix = str(flow[i][next]) + matrix
    res.append(matrix)


if flag:
    for t in res:
        print(t)
else:
    print(-1)



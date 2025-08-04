import sys
from collections import deque
input = sys.stdin.readline

N, P = map(int, input().split())
size = N+5
graph = [[] for _ in range(size)]
capacity = [[0]*size for _ in range(size)]
flow = [[0]*size for _ in range(size)]

for i in range(P):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    capacity[u][v] = 1
while True:
    qu = deque()
    qu.append(1)
    par = [-2]*size

    while qu and par[2] == -2:
        tmp = qu.popleft()
        for next in graph[tmp]:
            if capacity[tmp][next] - flow[tmp][next] > 0 and par[next] == -2:
                par[next] = tmp
                qu.append(next)

    if par[2] == -2:
        break
    end = 2
    while end != 1:
        flow[par[end]][end] += 1
        flow[end][par[end]] -= 1
        end = par[end]

res = 0
for i in range(1, N+1):
    res += flow[1][i]

print(res)


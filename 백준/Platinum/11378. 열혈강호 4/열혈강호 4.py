import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
size = N+M+5
graph = [[] for _ in range(size)]
capacity = [[0]*size for _ in range(size)]
flow = [[0]*size for _ in range(size)]

for i in range(1, N+1):
    capacity[0][i] = 1
    graph[0].append(i)
    n, *v = map(int, input().split())
    for t in v:
        graph[i].append(t+N)
        graph[t+N].append(i)
        capacity[i][t+N] = 1

for i in range(N+1, N+M+1):
    graph[i].append(-1)
    graph[-1].append(i)
    capacity[i][-1] = 1

graph[0].append(-3)
capacity[0][-3] = K
for k in range(1, N+1):
    graph[-3].append(k)
    capacity[-3][k] = K

while True:
    qu = deque()
    qu.append(0)
    par = [-2]*size

    while qu and par[-1] == -2:
        tmp = qu.popleft()
        for next in graph[tmp]:
            if capacity[tmp][next] - flow[tmp][next] > 0 and par[next] == -2:
                par[next] = tmp
                qu.append(next)

    if par[-1] == -2:
        break
    end = -1
    while end != 0:
        flow[par[end]][end] += 1
        flow[end][par[end]] -= 1
        end = par[end]

res = sum(flow[0])

print(res)


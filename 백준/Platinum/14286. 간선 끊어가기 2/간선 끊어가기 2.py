import sys
from collections import deque
input = sys.stdin.readline

N, P = map(int, input().split())
size = N+5
graph = [[] for _ in range(size)]
capacity = [[0]*size for _ in range(size)]
flow = [[0]*size for _ in range(size)]
res = 0
for i in range(P):
    u, v, m = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    capacity[u][v] = m
    capacity[v][u] = m

s, t = map(int, input().split())
while True:
    qu = deque()
    qu.append(s)
    par = [-2]*size

    while qu and par[t] == -2:
        tmp = qu.popleft()
        for next in graph[tmp]:
            if capacity[tmp][next] - flow[tmp][next] > 0 and par[next] == -2:
                par[next] = tmp
                qu.append(next)

    if par[t] == -2:
        break
    end = t
    f = 10**9
    while end != s:
        f = min(f, capacity[par[end]][end]-flow[par[end]][end])
        end = par[end]
    end = t
    while end != s:
        flow[par[end]][end] += f
        flow[end][par[end]] -= f
        end = par[end]
    res += f


print(res)


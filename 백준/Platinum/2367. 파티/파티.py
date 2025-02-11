import sys
from collections import deque
input = sys.stdin.readline

N, K, D = map(int, input().split())
size = N + D + 5
graph = [[] for _ in range(size)]
capacity = [[0]*size for _ in range(size)]
flow = [[0]*size for _ in range(size)]
for i in range(1, N+1):
    graph[0].append(i)
    graph[i].append(0)
    capacity[0][i] = K
dish = [0]+list(map(int, input().split()))
for i in range(1, D+1):
    capacity[N+i][-1] = dish[i]
    graph[N+i].append(-1)
    graph[-1].append(N+i)
for i in range(1, N+1):
    n, *lst = map(int, input().split())
    for j in lst:
        capacity[i][N+j] = 1
        graph[i].append(N+j)
        graph[N+j].append(i)


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

res = 0
for i in range(1, N+1):
    res += flow[0][i]

print(res)


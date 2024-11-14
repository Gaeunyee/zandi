import sys
from collections import deque
input = sys.stdin.readline

N, P = map(int, input().split())
size = 2 * N + 3
graph = [[] for _ in range(size)]
capacity = [[0]*size for _ in range(size)]
flow = [[0]*size for _ in range(size)]

for i in range(1, N+1):
    capacity[-i][i] = 1
    graph[-i].append(i)
    graph[i].append(-i)
capacity[-1][1] = 10**4 + 7
for _ in range(P): # end : - , start : +
    a, b = map(int, input().split())
    capacity[a][-b] = 1
    capacity[b][-a] = 1
    graph[a].append(-b)
    graph[-b].append(a)
    graph[b].append(-a)
    graph[-a].append(b)


while True:
    qu = deque()
    qu.append(-1)
    par = [0]*size

    while qu and par[-2] == 0:
        tmp = qu.popleft()
        for next in graph[tmp]:
            if capacity[tmp][next] - flow[tmp][next] > 0 and par[next] == 0:
                par[next] = tmp
                qu.append(next)


    if par[-2] == 0:
        break
    end = -2
    while end != -1:
        flow[par[end]][end] += 1
        flow[end][par[end]] -= 1
        end = par[end]

print(flow[-1][1])

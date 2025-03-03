import sys
from heapq import *
INF = 1 << 64 - 1
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N+2)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

p, q = map(int, input().split())
home = list(map(int, input().split()))
shop = list(map(int, input().split()))
TYPE = [0]*(N+2)
TYPE[-1] = 1
for i in shop:
    TYPE[i] = 1
    graph[-1].append((0, i))


def dijkstra(a):
    table = [INF]*(N+2)
    qu = []
    heappush(qu, (0, a))
    table[a] = 0
    while qu:
        time, tmp = heappop(qu)
        if table[tmp] < time:
            continue
        for d, nxt in graph[tmp]:
            if table[nxt] > time + d:
                table[nxt] = time+d
                heappush(qu, (time + d, nxt))
    return table


res_d, res_i = INF, INF
arr = dijkstra(-1)

home.sort()
for h in home:
    if arr[h] < res_d:
        res_d = arr[h]
        res_i = h

print(res_i)

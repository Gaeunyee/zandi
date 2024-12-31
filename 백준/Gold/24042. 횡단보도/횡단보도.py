import sys
from heapq import *
INF = 1 << 64 - 1
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

def dijkstra():
    table = [INF]*(N+1)
    qu = []
    heappush(qu, (0, 1))
    table[1] = 0
    while qu:
        time, tmp = heappop(qu)
        t = time % M
        if table[tmp] < time:
            continue
        for nxt, h in graph[tmp]:
            if table[nxt] > time + (h-t) % M + 1:
                table[nxt] = time + (h-t) % M + 1
                heappush(qu, (time + (h-t) % M + 1, nxt))
    print(table[N])

dijkstra()


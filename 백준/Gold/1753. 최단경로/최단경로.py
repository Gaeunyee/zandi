import sys
from heapq import *
input = sys.stdin.readline
INF = 10**9


def solve():
    V, E = map(int, input().split())
    K = int(input().strip())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    hq = []
    dist = [INF]*(V+1)
    dist[K] = 0
    heappush(hq, (0, K))
    while hq:
        d, tmp = heappop(hq)
        if d > dist[tmp]:
            continue
        for n, c in graph[tmp]:
            if d + c < dist[n]:
                dist[n] = d+c
                heappush(hq, (dist[n], n))

    for i in range(1, V+1):
        print(dist[i] if dist[i] != INF else "INF")


solve()

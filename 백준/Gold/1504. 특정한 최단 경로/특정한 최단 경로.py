import sys
from heapq import *
input = sys.stdin.readline
INF = 10**9

def dijkstra(start):
    hq = []
    dist = [INF] * (V + 1)
    dist[start] = 0
    heappush(hq, (0, start))
    while hq:
        d, tmp = heappop(hq)
        if d > dist[tmp]:
            continue
        for n, c in graph[tmp]:
            if d + c < dist[n]:
                dist[n] = d + c
                heappush(hq, (dist[n], n))
    return dist
def solve():
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    v1, v2 = map(int, input().split())
    d = dijkstra(1)
    st1, st2 = d[v1], d[v2]
    d = dijkstra(v1)
    vv, ed1 = d[v2], d[V]
    ed2 = dijkstra(v2)[V]
    res = min(st1+vv+ed2, st2+vv+ed1)

    print(res if res < INF else -1)

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

solve()

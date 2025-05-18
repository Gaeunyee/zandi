import sys
from heapq import *
input = sys.stdin.readline
INF = 10**9


def solve():
    V = int(input().strip())
    E = int(input().strip())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    s, e = map(int, input().split())
    hq = []
    dist = [INF]*(V+1)
    par = [-1]*(V+1)
    dist[s] = 0
    heappush(hq, (0, s))
    while hq:
        d, tmp = heappop(hq)
        if d > dist[tmp]:
            continue
        for n, c in graph[tmp]:
            if d + c < dist[n]:
                dist[n] = d+c
                par[n] = tmp
                heappush(hq, (dist[n], n))
    print(dist[e])
    tr = e
    res = []
    while tr != -1:
        res.append(tr)
        tr = par[tr]
    print(len(res))
    print(*res[::-1])


solve()

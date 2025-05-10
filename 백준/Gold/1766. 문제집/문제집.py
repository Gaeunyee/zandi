import sys
from heapq import *
input = sys.stdin.readline

INF = 10**9 + 7
size = 10**6 + 1
def solve():
    N, M = map(int, input().split())
    deg = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        deg[b] += 1
        graph[a].append(b)

    hq = []
    for i in range(1, N+1):
        if not deg[i]:
            heappush(hq, i)
    while hq:
        t = heappop(hq)
        print(t, end=' ')
        for n in graph[t]:
            deg[n] -= 1
            if not deg[n]:
                heappush(hq, n)


solve()


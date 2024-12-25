import sys
import heapq

INF = 10**7+7
input = sys.stdin.readline


N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
for i in range(M):
    start, end, time = map(int, input().split())
    lst[start].append((time, end))
    lst[end].append((time, start))

cost = 0
table = [(-1, INF)] + [(-1, INF)] * (N)
table[1] = (-1, 0)
route = []
def backTrack(end):
    tr = table[N][0]
    while tr != -1:
        route.append((tr, end))
        end = tr
        tr = table[tr][0]

def dijkstra(start, lst, u, v, table):
    visited = [0] * (N + 1)
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        d, temp = heapq.heappop(hq)
        if visited[temp]:
            continue
        visited[temp] = 1

        for dist, node in lst[temp]:
            if not (temp == u and node == v) and d+dist < table[node][1]:
                table[node] = (temp, d+dist)
                heapq.heappush(hq, (d+dist, node))
    return table[N][1]

dist = dijkstra(1, lst, -1, -1, table)
backTrack(N)

def solve():
    res = 0
    for u, v in route:
        table = [(-1, INF)] + [(-1, INF)] * (N)
        table[1] = (-1, 0)
        n = dijkstra(1, lst, u, v, table)
        if n == INF:
            print(-1)
            return
        res = max(res, n-dist)
    print(res)
    return

solve()


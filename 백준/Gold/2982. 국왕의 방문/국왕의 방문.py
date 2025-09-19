import sys
from heapq import *
input = sys.stdin.readline
INF = 10**9

class Edge:
    def __init__(self, end, time, l):
        self.end = end
        self.time = time
        self.l = l

N, M = map(int, input().split())
start, end, K, G = map(int, input().split())
graph = [[] for _ in range(N+1)]
time = [(-1, -1)]*(M+1)
path = list(map(int, input().split()))

for i in range(1, M+1):
    u, v, d = map(int, input().split())
    graph[u].append(Edge(v, -1, d))
    graph[v].append(Edge(u, -1, d))

t = 0
for i in range(G-1):
    d = 0
    for edge in graph[path[i]]:
        if edge.end == path[i+1]:
            edge.time = t
            d = edge.l
    for edge in graph[path[i+1]]:
        if edge.end == path[i]:
            edge.time = t
    t += d

visited = [INF]*(N+1)
visited[start] = K
qu = []
qu.append((K, start))
while qu:
    ti, t = heappop(qu)
    for edge in graph[t]:
        if edge.time != -1 and edge.time <= ti < edge.time+edge.l:
            nt = edge.time+2*edge.l

        else:
            nt = ti + edge.l
        if nt < visited[edge.end]:
            visited[edge.end] = nt
            heappush(qu, (nt, edge.end))
print(visited[end]-K)


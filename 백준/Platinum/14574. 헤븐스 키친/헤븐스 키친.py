import sys
from heapq import *
input = sys.stdin.readline

N = int(input().strip())
cook = [(0, 0)]
for _ in range(N):
    P, C = map(int, input().split())
    cook.append((P, C))

par = [i for i in range(N+1)]
qu = []
def find(a):
    if par[a] == a:
        return a
    par[a] = find(par[a])
    return par[a]

def union(a, b):
    x, y = find(a), find(b)
    if x != y:
        par[x] = y
        return True
    return False
for i in range(1, N+1):
    for j in range(i+1, N+1):
        t = (cook[i][1]+cook[j][1]) // abs(cook[i][0]-cook[j][0])
        heappush(qu, (-t, i, j))

graph = [[] for _ in range(N+1)]
cnt = 0
res = 0
while cnt < N-1 and qu:
    w, u, v = heappop(qu)
    if union(u, v):
        graph[u].append(v)
        graph[v].append(u)
        res -= w
        cnt += 1

visited = [False]*(N+1)


def dfs(p, t):
    visited[t] = True
    for n in graph[t]:
        if not visited[n]:
            dfs(t, n)
    if p != 0:
        print(p, t)

print(res)
dfs(0, 1)

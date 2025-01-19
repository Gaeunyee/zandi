import sys
from math import ceil, log
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N = int(input().strip())
graph = [[] for _ in range(N+1)]
for i in range(N):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

par = [-1]*(N+1)
isCycle = [0]*(N+1)
dist = [0]*(N+1)
def dfs(p, n):
    par[n] = p
    for next in graph[n]:
        if next != p and par[next] != -1:
            backTrack(n, next)
            return True
        if par[next] == -1:
            if dfs(n, next):
                return True
    return False


def backTrack(n, e):
    isCycle[e] = 1
    while n != e:
        isCycle[n] = 1
        n = par[n]

def solve(n, d):
    dist[n] = d
    for next in graph[n]:
        if not isCycle[next] and dist[next] == 0:
            solve(next, d+1)

dfs(0, 1)
for i in range(1, N+1):
    if isCycle[i]:
        solve(i, 0)

print(*dist[1:])



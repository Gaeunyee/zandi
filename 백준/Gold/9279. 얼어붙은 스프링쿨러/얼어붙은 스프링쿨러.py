import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
INF = 10**9+7

def dfs(u, g):
    visited[u] = 1
    s = 0
    for v, w in graph[u]:
        if not visited[v]:
            s += dfs(v, w)
    if s == 0:
        return g
    return min(s, g)




while True:
    k = input().split()
    if not k:
        break
    N, C = map(int, k)
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    dp = [0]*(N+1)
    visited = [0]*(N+1)
    print(dfs(C, INF))


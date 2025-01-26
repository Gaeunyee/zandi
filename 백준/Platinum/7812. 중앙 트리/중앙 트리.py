import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def setSize(p, t):
    global res
    visited[t] = 1
    for w, n in graph[t]:
        if not visited[n]:
            setSize(t, n)
            res += size[n]*w
    size[p] += size[t]

def dfs(t, cost):
    global res
    visited[t] = 1
    res = min(res, cost)
    for w, n in graph[t]:
        if not visited[n]:
            dfs(n, cost + (N-2*size[n])*w)

while True:
    N = int(input().strip())
    if N == 0:
        break
    graph = [[] for _ in range(N+2)]
    for _ in range(N-1):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))
    size = [1]*(N+2)
    res = 0
    visited = [0]*(N+2)
    setSize(N, 0)

    visited = [0] * (N + 2)
    dfs(0, res)
    print(res)



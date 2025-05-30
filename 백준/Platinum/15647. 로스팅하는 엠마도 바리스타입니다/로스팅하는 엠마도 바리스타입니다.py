import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5 * 3 + 1)

def setSize(t):
    global res
    size[t] = 1
    for w, n in graph[t]:
        if not size[n]:
            size[t] += setSize(n)
            res += size[n]*w
    return size[t]

def dfs(t, cost):
    global res
    visited[t] = cost
    res = min(res, cost)
    for w, n in graph[t]:
        if not visited[n]:
            dfs(n, cost + (N-2*size[n])*w)


N = int(input().strip())
if N == 1:
    print(0)
else:
    graph = [[] for _ in range(N + 2)]
    for _ in range(N - 1):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))
    size = [0] * (N + 2)
    res = 0
    setSize(1)

    visited = [0] * (N + 2)
    dfs(1, res)
    for i in range(1, N + 1):
        print(visited[i])



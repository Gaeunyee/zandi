import sys
sys.setrecursionlimit(10**5 + 3)
input = sys.stdin.readline


N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
dp = [0]*(N+1)


for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(t):
    dp[t] = 1
    for nxt in graph[t]:
        if not dp[nxt]:
            dp[t] += dfs(nxt)
    return dp[t]


dfs(R)
for _ in range(Q):
    U = int(input().strip())
    print(dp[U])


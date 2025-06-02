import sys

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[X].append((Y, K))

b = []
for i in range(1, N+1):
    if not len(graph[i]):
        b.append(i)

dp = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
def dfs(t):
    visited[t] = 1
    if not len(graph[t]):
        dp[t][t] = 1
        return
    for n, c in graph[t]:
        if not visited[n]:
            dfs(n)
        for i in b:
            dp[t][i] += c * dp[n][i]

dfs(N)
for i in b:
    if dp[N][i]:
        print(i, dp[N][i])

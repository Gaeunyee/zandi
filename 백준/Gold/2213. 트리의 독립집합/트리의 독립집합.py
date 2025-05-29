import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
INF = 10**9 + 7


N = int(input().strip())
m = [0]+list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(N+1)]
visited = [0]*(N+1)
def dfs(t):
    dp[t][1] = m[t]
    for n in graph[t]:
        if not dp[n][1]:
            dfs(n)
            dp[t][0] += max(dp[n])
            dp[t][1] += dp[n][0]

res = []
def backTrack(t, c):
    visited[t] = 1
    f = 0
    if c:
        for n in graph[t]:
            if not visited[n]:
                backTrack(n, f)
    else:
        if dp[t][1] > dp[t][0]:
            res.append(t)
            f = 1
        for n in graph[t]:
            if not visited[n]:
                backTrack(n, f)
dfs(1)
backTrack(1, 0)
print(max(dp[1]))
print(*sorted(res))



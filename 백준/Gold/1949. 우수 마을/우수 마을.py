import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input().strip())
lst = [-1] + list(map(int, input().split()))
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dp = [[0, 0] for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(par, tmp):
    visited[tmp] = True
    fl = 0
    dp[tmp][1] += lst[tmp]
    for nxt in adj[tmp]:
        if not visited[nxt]:
            fl = 1
            dfs(tmp, nxt)
    if fl == 0:
        dp[par][0] += dp[tmp][1]
        return
    dp[par][0] += max(dp[tmp][0], dp[tmp][1])
    dp[par][1] += dp[tmp][0]

dfs(0, 1)
print(max(dp[1]))
import sys

input = sys.stdin.readline
INF = 10 ** 6
sys.setrecursionlimit((10**5)*3)
N = int(input().strip())
dp = [1]*(N+2)
visited = [0]*(N+2)
graph = [[] for _ in range(N+2)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(p, t):
    visited[t] = 1
    dp[t] = p
    for nxt in graph[t]:
        if not visited[nxt]:
            dfs(p+1, nxt)

dfs(0, 0)
res = ''
for i in range(N-1, 0, -1):
    if (N-dp[i]) % 2 == 1:
        res += '0'
    else:
        res += '1'
print(res)



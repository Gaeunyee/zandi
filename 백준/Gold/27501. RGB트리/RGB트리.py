import sys

INF = 10**7+7
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().strip())
graph = [[] for _ in range(N+1)]
dp = [[0, 0, 0]]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N):
    r, g, b = map(int, input().split())
    dp.append([r, g, b])
it = [(1, 2), (0, 2), (0, 1)]
visited = [False]*(N+1)
def dfs(tmp):
    visited[tmp] = True
    for nxt in graph[tmp]:
        if not visited[nxt]:
            dfs(nxt)

            for i in range(3):
                dp[tmp][i] += max(dp[nxt][it[i][0]], dp[nxt][it[i][1]])

def backTrack(c, tmp):
    visited[tmp] = True
    if tmp != 1:
        res[tmp] = it[c][0]
    for k in it[c]:
        if dp[tmp][res[tmp]] < dp[tmp][k]:
            res[tmp] = k
    for nxt in graph[tmp]:
        if not visited[nxt]:
            backTrack(res[tmp], nxt)


dfs(1)
res = [-1]*(N+1)
col, val = 0, 0
for i in range(3):
    if val < dp[1][i]:
        col = i
        val = dp[1][i]
print(val)
res[1] = col
visited = [False]*(N+1)
backTrack(0, 1)

for i in res[1:]:
    if i == 0:
        print('R', end='')
    if i == 1:
        print('G', end='')
    if i == 2:
        print('B', end='')

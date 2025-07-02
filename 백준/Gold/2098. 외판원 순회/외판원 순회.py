import sys
from collections import deque
input = sys.stdin.readline

INF = 10**9 + 7

N = int(input().strip())
dist = []
for _ in range(N):
    dist.append(list(map(int, input().split())))

dp = [[INF]*(1 << N) for _ in range(N)]
qu = deque()
dp[0][1] = 0
qu.append((1, 0))
while qu:
    tr, t = qu.popleft()
    for i in range(N):
        if dist[t][i] and not tr & (1 << i):
            n = tr | (1 << i)
            if dp[i][n] == INF:
                qu.append((n, i))
            dp[i][n] = min(dp[i][n], dp[t][tr] + dist[t][i])

res = INF
for i in range(N):
    if dist[i][0]:
        res = min(res, dp[i][(1<<N) - 1]+dist[i][0])
print(res)


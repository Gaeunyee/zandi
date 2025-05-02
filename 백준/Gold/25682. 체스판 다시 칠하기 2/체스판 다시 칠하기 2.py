import sys
input = sys.stdin.readline


def getsum(x, y, k):
    return dp[x][y] - dp[x-k][y] - dp[x][y-k] + dp[x-k][y-k]


N, M, K = map(int, input().split())
arr = ['']
for _ in range(N):
    arr.append('$'+input().strip())

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        if arr[i][j] == 'B' and (i+j)%2 == 1:
            dp[i][j] += 1
        elif arr[i][j] == 'W' and (i+j)%2 == 0:
            dp[i][j] += 1

res = K**2 + 7
for i in range(K, N+1):
    for j in range(K, M+1):
        res = min(res, getsum(i, j, K))

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        if arr[i][j] == 'B' and (i + j) % 2 == 0:
            dp[i][j] += 1
        elif arr[i][j] == 'W' and (i + j) % 2 == 1:
            dp[i][j] += 1

for i in range(K, N + 1):
    for j in range(K, M + 1):
        res = min(res, getsum(i, j, K))




print(res)

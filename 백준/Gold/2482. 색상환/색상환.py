import sys

input = sys.stdin.readline
SIZE = 21
m = 10**9 + 3

N = int(input().strip())
K = int(input().strip())
dp = [[0]*4 for _ in range(K+1)]
dp[0] = [0, 0, 0, 1]
dp[1] = [1, 0, 0, 0]
for _ in range(1, N):
    for k in range(K, -1, -1):
        dp[k][1] += dp[k][0]
        dp[k][3] += dp[k][2]
        if k >= 1:
            dp[k][0] = dp[k-1][1]
            dp[k][2] = dp[k-1][3]
        for j in range(4):
            dp[k][j] %= m


print((dp[K][1]+dp[K][2]+dp[K][3])%m)

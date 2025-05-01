import sys
input = sys.stdin.readline

m = 10**9

dp = [[[0]*10 for _ in range(10)] for _ in range(101)]
for i in range(10):
    dp[1][i][i] = 1
N = int(input().strip())
for i in range(2, N+1):
    for j in range(10):
        for k in range(10):
            if j != 0:
                dp[i][j][k] += dp[i-1][j-1][k]
            if j != 9:
                dp[i][j][k] += dp[i-1][j+1][k]
            dp[i][j][k] %= m

res = 0
for i in range(1, 10):
    res += sum(dp[N][i])
    res %= m
print(res)


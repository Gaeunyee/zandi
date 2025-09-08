import sys
input = sys.stdin.readline
mod = 987654321

N = int(input())
dp = [0]*(N+1)
dp[0] = 1
dp[2] = 1
for i in range(4, N+1, 2):
    for j in range(1, i//2+1):
        dp[i] += dp[i-j*2]*dp[(j-1)*2]
        dp[i] %= mod

print(dp[N])

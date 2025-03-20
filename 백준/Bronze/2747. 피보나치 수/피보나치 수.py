import sys
input = sys.stdin.readline


dp = [0]*46
dp[0], dp[1] = 0, 1
for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[int(input().strip())])

import sys
input = sys.stdin.readline


N = int(input().strip())
arr = list(map(int, input().split()))

dp = [0]*N
dp[0] = arr[0]
for i in range(1, N):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp))

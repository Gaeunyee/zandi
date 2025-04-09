import sys
input = sys.stdin.readline


N = int(input().strip())
arr = list(map(int, input().split()))

dp = [0, arr[0], 0, 0, 0]
for i in range(1, N):
    dp = [dp[0], max(arr[i], dp[1]+arr[i]), max(dp[1], dp[2]), max(dp[2]+arr[i], dp[3]+arr[i]), max(dp[4], dp[3])]

print(max(dp) + sum(arr))

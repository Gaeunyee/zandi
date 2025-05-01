import sys
input = sys.stdin.readline
INF = 10**9 + 7

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(int(input().strip()))
dp = [0, arr[0], -INF]
for i in range(1, n):
    dp = [max(dp), dp[0]+arr[i], dp[1]+arr[i]]

print(max(dp))



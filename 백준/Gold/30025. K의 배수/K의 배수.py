import sys
input = sys.stdin.readline
SIZE = 10**9 + 7

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0]*K for _ in range(M+1)]
for i in arr:
    if i != 0:
        dp[1][i%K] += 1
for i in range(1, M):
    for a in arr:
        for r in range(K):
            k = (r*10)%K
            dp[i+1][(a+k)%K] = (dp[i+1][(a+k)%K] + dp[i][r])%SIZE

print(dp[M][0])



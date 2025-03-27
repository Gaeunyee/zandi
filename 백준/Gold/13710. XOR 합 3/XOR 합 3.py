import sys
input = sys.stdin.readline


N = int(input().strip())
A = list(map(int, input().split()))
dp = [[0]*31 for _ in range(N)]
res = [0]*(N+1)
for i in range(31):
    if A[0] & (1 << i):
        dp[0][i] = 1
res[0] = A[0]
for i in range(1, N):
    for j in range(31):
        if A[i] & (1 << j):
            dp[i][j] = i-dp[i-1][j] + 1
        else:
            dp[i][j] = dp[i-1][j]
    for j in range(31):
        res[i] += dp[i][j] * (1 << j)
    res[i] += res[i-1]

print(res[N-1])


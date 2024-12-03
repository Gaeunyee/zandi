import sys

input = sys.stdin.readline
size = 5 * 10**5 + 1


N = int(input().strip())

block = [-1] + list(map(int, input().split()))
dp = [[-1]*size for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    for j in range(size):
        if dp[i-1][j] != -1:
            dp[i][j+block[i]] = max(dp[i][j+block[i]], dp[i-1][j] + block[i])
            dp[i][abs(j - block[i])] = max(dp[i][abs(j - block[i])],
                                           dp[i-1][j], dp[i-1][j]-j+block[i])
            dp[i][j] = max(dp[i][j], dp[i-1][j])

if dp[N][0] != 0:
    print(dp[N][0])
else:
    print(-1)


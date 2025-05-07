import sys
input = sys.stdin.readline

T = int(input().strip())
INF = 10**9 + 7
for _ in range(T):
    N = int(input().strip())
    lst = list(map(int, input().split())) + [0]
    for i in range(1, N):
        lst[i] += lst[i-1]
    dp = [[INF]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for i in range(N-1, -1, -1):
        for j in range(i+1, N):
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

            dp[i][j] += lst[j] - lst[i - 1]


    print(dp[0][N-1])


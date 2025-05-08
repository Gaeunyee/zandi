import sys
input = sys.stdin.readline

INF = 10**9 + 7
def solve():
    N = int(input().strip())
    lst = []
    for i in range(N):
        lst.append(tuple(map(int, input().split())))
    dp = [[INF]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for i in range(N-1, -1, -1):
        for j in range(i+1, N):
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + lst[i][0]*lst[k][1]*lst[j][1])

    print(dp[0][N-1])

solve()


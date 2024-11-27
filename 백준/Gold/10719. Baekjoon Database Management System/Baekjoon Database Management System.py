import sys
input = sys.stdin.readline
INF = 10**7
T = int(input().strip())


for _ in range(T):
    n, m, c = map(int, input().split())
    costs = [-1] + list(map(int, input().split()))
    tasks = [1] + list(map(int, input().split()))
    dp = [[INF]*(m+1) for _ in range(n+1)]
    dp[0] = [0]+[INF]*(m)
    for i in range(n):
        for j in range(0, m+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+costs[tasks[i+1]])
            dp[i+1][tasks[i+1]] = min(dp[i+1][tasks[i+1]],
                                      dp[i][j]+c, dp[i][tasks[i+1]])
    print(min(dp[n]))



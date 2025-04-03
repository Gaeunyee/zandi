import sys
input = sys.stdin.readline
INF = 10**9+7

def solve():
    N, K = map(int, input().split())
    lst = [(0, 0)]
    for _ in range(N):
        lst.append(tuple(map(int, input().split())))
    dp = [[-INF]*(K+1) for _ in range(N+1)]  # 담은 무게 기준
    dp[0][0] = 0
    for i in range(1, N+1):
        for j in range(K+1):
            dp[i][j] = dp[i-1][j]
            if j >= lst[i][0]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-lst[i][0]] + lst[i][1])

    print(max(dp[N]))

solve()

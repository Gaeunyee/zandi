import sys
input = sys.stdin.readline


def solve():
    inf = 10**14
    N = int(input().strip())
    N += 1
    lst = [0]+list(map(int, input().split()))
    dp = [[-inf]*4 for _ in range(N)]
    dp[0][1] = lst[0]
    for i in range(1, N):
        dp[i][1] = dp[i-1][1] + lst[i]
    
    m = [-inf]*4
    for i in range(1, N):
        for j in range(2, 4):
            dp[i][j] = max(dp[i-1][j]+lst[i], m[j-1] + lst[i])
        for k in range(1, 4):
            m[k] = max(m[k], dp[i-1][k])
    
    res = -inf
    for i in range(N):
        res = max(res, max(dp[i]))
    
    print(res)
    
solve()

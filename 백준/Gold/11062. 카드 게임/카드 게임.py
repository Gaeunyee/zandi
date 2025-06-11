import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    lst = list(map(int, input().split()))
    s = [0]
    for i in range(N):
        s.append(s[-1]+lst[i])
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        dp[i+1][i+1] = lst[i]
    for i in range(N, 0, -1):
        for j in range(i+1, N+1):
            dp[i][j] = s[j]-s[i-1] - min(dp[i+1][j], dp[i][j-1])

    print(dp[1][N])


T = int(input().strip())
for _ in range(T):
    solve()


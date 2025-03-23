import sys
input = sys.stdin.readline


SIZE = 1300
N, S = map(int, input().split())
dp = [[0]*SIZE for _ in range(N+5)]
dp[1][0], dp[2][0] = 1, 1
for i in range(2, N):
    for k in range(1, N-i+1):
        a = (1+k)*k//2
        for j in range(S + 1):
            if dp[i][j]:
                dp[i+k][j+a] = 1

print(dp[N][S])



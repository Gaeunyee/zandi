import sys
input = sys.stdin.readline

INF = 10**9 + 7
size = 10001
def solve():
    N, K = map(int, input().split())
    dp = [0]*(K+1)
    dp[0] = 1
    for _ in range(N):
        i = int(input().strip())

        for k in range(i, K+1):
            dp[k] += dp[k-i]


    print(dp[K])

solve()


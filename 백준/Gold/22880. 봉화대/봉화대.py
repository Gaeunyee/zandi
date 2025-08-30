import sys
input = sys.stdin.readline

N = int(input())
mod = 10**9 + 7
lst = list(map(int, input().split()))
k = []
m = -1
cnt = 0
for i in range(N):
    if lst[i] > m:
        m = lst[i]
        k.append((lst[i], cnt))
        cnt = 0
    else:
        cnt += 1

dp = [[0, 0] for _ in range(len(k))]
dp[0] = [0, 1]
for i in range(1, len(k)):
    dp[i][0] = (dp[i-1][0]+dp[i-1][1])%mod
    dp[i][1] = ((dp[i-1][0]+dp[i-1][1])*(k[i][1]+1))%mod

print(sum(dp[-1])%mod)

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
dp = [[-10**9]*(M+1) for _ in range(N*5+1)]
dp_n = [[-10**9]*(M+1) for _ in range(N*5+1)]
dp[0][0] = 0
lst = []
for _ in range(N):
    c, m, p = map(int, input().split())
    lst.append((c, m, p))


for c, m, p in lst:
    for sp in range(N*5+1-p):
        for sc in range(M+1):
            dp_n[sp][sc] = max(dp_n[sp][sc], dp[sp][sc])
            tp, tc = sp+p, min(M, sc+c)
            dp_n[tp][tc] = max(dp_n[tp][tc], dp[sp][sc]+m)
    dp, dp_n = dp_n, dp

res = -1
for i in range(N*5+1):
    if dp[i][M] >= K:
        res = i
        break

print(res)


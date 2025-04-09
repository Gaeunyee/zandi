import sys
input = sys.stdin.readline
INF = 10**5

N = int(input().strip())
M = int(input().strip())
arr = []

for _ in range(M):
    u, v = map(int, input().split())
    arr.append((u, v))

isin = [0]
arr.append((N+1, N+1))
arr.sort(key=lambda x: x[1])

dp = [i for i in range(N+2)]
for i in range(M+1):
    st, ed = arr[i]
    for j in isin:
        if j >= st:
            break
        dp[ed] = min(dp[ed], max(st-j-1, dp[j]))
    if isin[-1] < ed:
        isin.append(ed)


print(dp[N+1])

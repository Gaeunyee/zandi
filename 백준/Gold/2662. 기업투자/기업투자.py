import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
money = [[0] for _ in range(M+1)]
for _ in range(N):
    l = list(map(int, input().split()))
    for k in range(1, M+1):
        money[k].append(l[k])

dp = [[0]*(N+1) for i in range(M+1)]
for i in range(1, M+1):
    for j in range(1, N+1):
        for k in range(j+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j-k] + money[i][k])
res = -1
for i in range(1, M+1):
    if dp[i][N] > res:
        res = dp[i][N]
print(res)
last = M
a = N
iv = []
while last != 0:
    for i in range(a+1):
        if dp[last-1][a-i]+money[last][i] == dp[last][a]:
            iv.append(i)
            a -= i
            last -= 1
            break

while iv:
    print(iv.pop(), end=' ')



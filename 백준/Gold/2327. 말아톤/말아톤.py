import sys
input = sys.stdin.readline

INF = 10**9 + 7

H, N = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split()))) # (키, 속도)

dp = [-1]*(H+1)  # 팀에서 가장 느린 사람
dp[0] = INF
for i in range(N):
    for j in range(H, lst[i][0], -1):
        if dp[j-lst[i][0]] == -1:
            continue
        dp[j] = max(min(dp[j-lst[i][0]], lst[i][1]), dp[j])
    dp[lst[i][0]] = max(dp[lst[i][0]], lst[i][1])

print(dp[H])



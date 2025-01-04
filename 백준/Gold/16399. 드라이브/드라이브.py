import sys
input = sys.stdin.readline
INF = (1<<64)-1

C, E, D = map(int, input().split())
N = int(input().strip())
s = [0] + list(map(int, input().split()))  # N
p = [0] + list(map(int, input().split()))  # N

dp = [[INF]*(C+1) for _ in range(N+1)]
dp[0][C] = 0
flag = 1
for i in range(1, N+1):
    for e in range(C+1):
        if s[i]*E > C:
            flag = 0
            break
        for f in range(s[i]*E, min(C+1, s[i]*E+e+1)):
            # 현재 연료 = 이전 연료-거리*연비
            # e = 추가하는 양 + 이전 연료-거리*연비
            dp[i][e] = min(dp[i][e], dp[i-1][f] + p[i]*(s[i]*E+e-f))
r = D-sum(s)
if r*E > C:
    flag = 0
if flag:
    print(min(dp[N][r*E:]))
else:
    print(-1)


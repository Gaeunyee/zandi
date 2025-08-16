import sys
input = sys.stdin.readline
INF = 10**6

N, X, Y = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))

dp = [[INF]*(Y+1) for _ in range(X+1)]
res = [[INF]*(Y+1) for _ in range(X+1)]
dp[0][0] = 0
for k in range(N):
    x, y = lst[k]
    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            nx, ny = min(X, x+i), min(Y, y+j)
            if dp[i][j] != INF:
                if dp[nx][ny] > dp[i][j]+1:
                    dp[nx][ny] = dp[i][j]+1
                    res[nx][ny] = k+1

r = -1 if res[X][Y] == INF else res[X][Y]
if r != -1:
    print(dp[X][Y])
    print(r)
else:
    print(r)

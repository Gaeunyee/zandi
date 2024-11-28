import sys
from collections import deque

input = sys.stdin.readline
INF = 10**5
#sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
box = [[-1]]
for _ in range(N):
    box.append(list(map(int, input().split())))
sum_box = list(map(sum, box))

size = 1 << M
dp = [[INF]*size for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(size):
        for k in range(M):
            if j & (1 << k):
                continue
            else:
                dp[i+1][j | (1 << k)] = min(dp[i+1][j | (1 << k)],
                                            dp[i][j]+sum_box[i+1]-box[i+1][k])
        dp[i+1][j] = min(dp[i+1][j], dp[i][j]+sum_box[i+1])
print(dp[N][size-1])



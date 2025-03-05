import sys
from heapq import *
INF = 1 << 64 - 1
input = sys.stdin.readline

N, T, M = map(int, input().split())
graph = [[[] for _ in range(T+2)] for _ in range(N+1)]
S, E = map(int, input().split())


dp = [[INF]*(N+1) for _ in range(T+1)]
dp[0][S] = 0
for time in range(T):
    for tmp in range(N):
        dp[time+1][tmp] = dp[time][tmp]
    for edge in range(M):
        a, b, c = map(int, input().split())
        dp[time+1][b] = min(dp[time+1][b], dp[time][a]+c)
        dp[time + 1][a] = min(dp[time + 1][a], dp[time][b] + c)

print(dp[T][E] if dp[T][E] != INF else -1)


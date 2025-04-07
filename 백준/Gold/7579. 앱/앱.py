import sys
input = sys.stdin.readline
SIZE = 10**4 + 7
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
INF = 10**9 + 7
dp = [-1]*SIZE
dp[0] = 0
for i in range(N):
    for j in range(SIZE-1, cost[i], -1):
        if dp[j-cost[i]] != -1:
            dp[j] = max(dp[j], dp[j-cost[i]] + memory[i])
    dp[cost[i]] = max(dp[cost[i]], dp[0] + memory[i])

for i in range(SIZE):
    if dp[i] >= M:
        print(i)
        break





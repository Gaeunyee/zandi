import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
INF = 10**9+7
N = int(input().strip())
graph = [(0, 0, 0)]
for i in range(N):
    line = input().strip()
    l, r = -1, -1
    for k in range(N):
        if line[k] == '1':
            l = k
            break
    for k in range(N-1, -1, -1):
        if line[k] == '1':
            r = k
            break
    if r != -1:
        graph.append((i, l, r))

size = len(graph)-1
dp = [[INF, INF] for _ in range(N+1)]
dp[0] = [0, 0]
for i in range(1, size+1):
    h, s, e = graph[i]
    k, l, r = graph[i-1]
    if h == 0:
        dp[i] = [INF, e]
        continue
    elif h != N-1:
        if h-k > 1 or e <= l:
            dp[i][0] = min(dp[i][0], dp[i-1][0] + abs(l-e) + e-s)
        dp[i][0] = min(dp[i][0], dp[i-1][1] + abs(r-e) + e-s)
    dp[i][1] = min(dp[i][1], dp[i-1][0] + abs(l-s) + e-s)
    if h-k > 1 or r <= s:
        dp[i][1] = min(dp[i][1], dp[i-1][1] + abs(r-s) + e-s)


if dp[size][0] >= INF and dp[size][1] >= INF:
    print(-1)
else:
    print(min(dp[size][0] + 2*N - 1 - graph[size][1], dp[size][1] + 2*N - 1 - graph[size][2]))



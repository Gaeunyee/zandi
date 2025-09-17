import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
lst = [0]
graph = [[] for _ in range(N+1)]
deg = [0]
qu = deque()
for i in range(1, N+1):
    p = list(map(int, input().split()))
    lst.append(p[0])
    deg.append(len(p)-2)
    if len(p) == 2:
        qu.append(i)
    for j in p[1:-1]:
        graph[j].append(i)

dp = [0]*(N+1)
while qu:
    t = qu.popleft()
    for n in graph[t]:
        dp[n] = max(dp[n], dp[t]+lst[t])
        deg[n] -= 1
        if deg[n] == 0:
            qu.append(n)

for i in range(1, N+1):
    print(dp[i]+lst[i])

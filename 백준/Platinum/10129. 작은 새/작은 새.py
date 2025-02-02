import sys
from collections import deque
input = sys.stdin.readline
mod = 10**9 + 7
N = int(input().strip())
tree = list(map(int, input().split()))
q = int(input().strip())
for _ in range(q):
    k = int(input().strip())
    dp = [0]*N
    qu = deque()
    qu.append(0)
    for i in range(1, N):
        while qu and i-qu[0] > k:
            qu.popleft()
        dp[i] = dp[qu[0]] + (1 if tree[qu[0]] <= tree[i] else 0)
        while qu and (dp[qu[-1]] > dp[i] or (dp[qu[-1]] == dp[i] and tree[qu[-1]] <= tree[i])):
            qu.pop()
        qu.append(i)
    print(dp[N-1])


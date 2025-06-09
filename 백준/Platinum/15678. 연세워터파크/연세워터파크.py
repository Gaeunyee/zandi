import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, D = map(int, input().split())
    dp = list(map(int, input().split()))

    qu = deque()
    qu.append(0)
    for i in range(1, N):
        while qu[0] < i-D:
            qu.popleft()
        dp[i] += dp[qu[0]] if dp[qu[0]] > 0 else 0
        while qu and dp[qu[-1]] < dp[i]:
            qu.pop()
        qu.append(i)

    print(max(dp))

solve()


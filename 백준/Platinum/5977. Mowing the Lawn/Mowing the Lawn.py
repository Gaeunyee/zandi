import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    lst = [0]
    for _ in range(N):
        lst.append(int(input().strip()))  # 수
    qu = deque()
    qu.append((1, 2))
    dp = [0]*(N+2)
    s = [0]
    for i in lst[1:]:
        s.append(s[-1]+i)
    s.append(0)
    dp[1] = lst[1]
    for i in range(2, N+1):
        while qu and i - qu[0][0] > K-1:
            qu.popleft()
        t, d = max(dp[i-2], dp[i-3])+lst[i], max(2, 3, key=lambda x: dp[i-x])
        while qu and dp[i-2]+lst[i] >= dp[qu[-1][0]-qu[-1][1]]+s[i]-s[qu[-1][0]-1]:
            qu.pop()
        qu.append((i, d))
        dp[i] = dp[qu[0][0]-qu[0][1]]+s[i]-s[qu[0][0]-1]
    print(dp[N])



solve()



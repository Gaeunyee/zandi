import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, M, C, D = map(int, input().split())
    lst = list(map(int, input().split()))
    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[0] = [M - abs(lst[0]-i) for i in range(M+1)]
    for t in range(1, N):
        qu = [deque() for _ in range(C)]
        for i in range(1, min(D+2, M+1)):
            while qu[i % C] and dp[t-1][qu[i % C][-1]] < dp[t-1][i]:
                qu[i % C].pop()
            qu[i % C].append(i)
        for i in range(1, M+1):
            while qu[i % C][0] < i-D:
                qu[i % C].popleft()
            dp[t][i] = dp[t-1][qu[i % C][0]] + M - abs(lst[t]-i)
            if i+D+1 <= M:
                while qu[(i+D+1) % C] and dp[t-1][qu[(i+D+1) % C][-1]] < dp[t-1][i+D+1]:
                    qu[(i+D+1) % C].pop()
                qu[(i+D+1) % C].append(i+D+1)

    print(max(dp[N-1]))

solve()


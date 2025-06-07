import sys
from math import log
from collections import deque
input = sys.stdin.readline


def solve():
    N = int(input().strip())
    lst = []
    for _ in range(N):
        lst.append(int(input().strip()))
    K = int(input().strip())
    size = 1 << N
    dp = [[0] * size for _ in range(K)]
    leng = [10**len(str(lst[i])) for i in range(N)]
    for i in range(N):
        lst[i] %= K
    visited = [0] * size
    qu = deque()
    qu.append(0)
    dp[0][0] = 1
    while qu:
        mask = qu.popleft()
        for i in range(N):
            if not mask & (1 << i):
                n = mask | (1 << i)
                if not visited[n]:
                    visited[n] = 1
                    qu.append(n)
                for j in range(K):
                    dp[(((j * leng[i]) % K) + lst[i]) % K][n] += dp[j][mask]

    s = 0
    for i in range(K):
        s += dp[i][(1 << N) - 1]
    p = dp[0][(1 << N) - 1]
    a, b = s, p
    while b != 0:
        a, b = b, a % b
    print(f'{p // a}/{s // a}')


solve()

import sys
from heapq import *

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    size = N*100 + 1
    lst = [(0, 0)]
    for _ in range(N):
        lst.append(tuple(map(int, input().split())))
    dp_p = [0]*size
    for i in range(1, N+1):
        dp = [size] * size
        for j in range(size):
            if j >= lst[i][0]:
                dp[j] = min(dp[j], dp_p[j-lst[i][0]])
            dp[j] = min(dp[j], dp_p[j] + lst[i][1])
        dp_p = dp
    res = size
    for j in range(size):
        res = min(res, max(dp_p[j], j))
    print(res)



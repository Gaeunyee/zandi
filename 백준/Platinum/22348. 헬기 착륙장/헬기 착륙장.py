import sys
from collections import deque
from math import *
input = sys.stdin.readline

# N, M = map(int, input().split())
T = int(input().strip())
size = 500
m = 10**9 + 7
for _ in range(T):
    a, b = map(int, input().split())
    dp = [[0]*(a+1) for _ in range(size)]
    s_ab = 0
    dp[0][0] = 1
    for i in range(1, size):
        s_ab += i
        for j in range(a+1):
            if s_ab-j <= b:
                dp[i][j] += dp[i-1][j]
            if a >= j-i >= 0:
                dp[i][j] += dp[i-1][j-i]
    res = 0
    for l in range(1, size):
        res = (res + sum(dp[l])) % m
    print(res)


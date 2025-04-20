import sys
input = sys.stdin.readline


N = int(input().strip())
dp = [0]*(N+1)
dp[2], dp[3] = 1, 1
def mex(lst):
    for i in range(11):
        if lst[i] == 0:
            return i


for i in range(4, N+1):
    m = [0]*11
    M = i-2
    for j in range(M//2+1):
        r = dp[j] ^ dp[M - j]
        if r < 11:
            m[r] = 1
    dp[i] = mex(m)


print(1 if dp[N] != 0 else 2)


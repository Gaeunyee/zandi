import sys
input = sys.stdin.readline
size = 2**10
mod = 1000000000
N = int(input())
dp = [[0]*size for _ in range(10)]
for i in range(1, 10):
    dp[i][1<<i] = 1

for _ in range(N-1):
    dp_n = [[0]*size for _ in range(10)]
    for i in range(10):
        for j in range(size):
            if i < 9:
                dp_n[i+1][j|(1<<(i+1))] += dp[i][j]
                dp_n[i + 1][j | (1 << (i + 1))] %= mod
            if i > 0:
                dp_n[i-1][j | (1 << (i-1))] += dp[i][j]
                dp_n[i - 1][j | (1 << (i - 1))] %= mod
    dp = dp_n

res = 0
for i in range(10):
    res += dp[i][size-1]
    res %= mod
print(res)

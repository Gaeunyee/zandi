import sys
input = sys.stdin.readline


N = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]
a.sort(reverse=True)
b.sort(reverse=True)
def vs(a, b):
    if a > b:
        return 2
    elif a == b:
        return 1
    return 0
for i in range(N):
    for j in range(i+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j-1]+vs(a[j], b[i]), dp[i-1][j])

print(max(dp[N-1]))
import sys
input = sys.stdin.readline


def getsum(x, y, k):
    s = dp[x][y] - dp[x-k][y] - dp[x][y-k] + dp[x-k][y-k]
    s0 = dp_0[x][y] - dp_0[x-k][y] - dp_0[x][y-k] + dp_0[x-k][y-k]
    if k**2 == s:
        return 3
    elif k**2 == s0:
        return 2
    elif k**2 == -s:
        return 1
    return 0


N = int(input().strip())
arr = [[]]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))


dp = [[0]*(N+1) for _ in range(N+1)]
dp_0 = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]
        dp_0[i][j] = dp_0[i - 1][j] + dp_0[i][j - 1] - dp_0[i - 1][j - 1] + (1 if not arr[i][j] else 0)

res = [0, 0, 0, 0]
def solve(x, y, size):
    gs = getsum(x, y, size)
    if gs:
        res[gs] += 1
        return
    s = size//3
    solve(x, y-s, s)
    solve(x, y-2*s, s)
    solve(x-s, y, s)
    solve(x-2*s, y, s)
    solve(x-s, y-s, s)
    solve(x-2*s, y-2*s, s)
    solve(x-s, y-2*s, s)
    solve(x-2*s, y-s, s)
    solve(x, y, s)

solve(N, N, N)
print(res[1])
print(res[2])
print(res[3])

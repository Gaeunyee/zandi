import sys
input = sys.stdin.readline


def getsum(x, y, k):
    s = dp[x][y] - dp[x-k][y] - dp[x][y-k] + dp[x-k][y-k]
    if k**2 == s:
        return 1
    elif not s:
        return 2
    return 0


N = int(input().strip())
arr = [[]]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))


dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]

res = [0, 0, 0]
def solve(x, y, size):
    global res
    gs = getsum(x, y, size)
    if gs:
        res[gs] += 1
        return
    s = size//2
    solve(x, y-s, s)
    solve(x-s, y, s)
    solve(x-s, y-s, s)
    solve(x, y, s)

solve(N, N, N)
print(res[2])
print(res[1])

import sys
input = sys.stdin.readline
SIZE = 10**7
sys.setrecursionlimit(10**5*3)
M, N = map(int, input().split())
dp = [[-1]*N for _ in range(M)]

dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    s = 0
    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] > graph[x][y]:
                s += dfs(nx, ny)
    dp[x][y] = s
    return dp[x][y]




dp[0][0] = 1
dfs(M-1, N-1)
print(dp[M-1][N-1])


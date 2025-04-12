import sys
sys.setrecursionlimit(10**6+7)
input = sys.stdin.readline
INF = 10 ** 6

N, M = map(int, input().split())
graph = []
dp = [[-1]*M for _ in range(N)]
for _ in range(N):
    graph.append(input().strip())

def func(x, y):
    if graph[x][y] == 'N':
        return x-1, y
    elif graph[x][y] == 'E':
        return x, y+1
    elif graph[x][y] == 'S':
        return x+1, y
    else:
        return x, y-1

def dfs(x, y):
    global dp
    nx, ny = func(x, y)
    if dp[x][y] == -1:
        dp[x][y] = 0
        if dfs(nx, ny):
            dp[x][y] = 1
            return 1
        else:
            dp[x][y] = 1
            return 0
    elif dp[x][y] == 0:
        return 1
    else:
        return 0


res = 0
for i in range(N):
    for j in range(M):
        if dp[i][j] == -1:
            res += dfs(i, j)

print(res)


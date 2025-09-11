import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[10**9]*(N+1) for _ in range(N+1)]
res = [[-1]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v, d = map(int, input().split())
    matrix[u][v] = d
    matrix[v][u] = d
    res[u][v] = v
    res[v][u] = u
for i in range(1, N+1):
    matrix[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]
                res[i][j] = res[i][k]


for i in range(1, N+1):
    for j in range(1, N+1):
        print(res[i][j] if res[i][j] != -1 else '-', end=' ')
    print()

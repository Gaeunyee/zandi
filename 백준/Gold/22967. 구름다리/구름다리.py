import sys
input = sys.stdin.readline

INF = 10**9


N = int(input().strip())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

if N <= 4:
    res = []
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if not graph[i][j]:
                res.append((i, j))
    print(len(res))
    print(1)
    for u, v in res:
        print(u, v)

else:
    res = []
    for i in range(2, N+1):
        if not graph[1][i]:
            res.append((1, i))
    print(len(res))
    print(2)
    for u, v in res:
        print(u, v)



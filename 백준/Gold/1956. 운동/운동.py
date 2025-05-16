import sys
input = sys.stdin.readline

INF = 10**9

def solve():
    N, M = map(int, input().split())

    dist = [[INF]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        dist[a][b] = min(dist[a][b], c)
    for i in range(1, N+1):
        dist[i][i] = 0

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    res = INF
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            res = min(res, dist[i][j]+dist[j][i])
    print(res if res != INF else -1)
    return


solve()






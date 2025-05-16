import sys
input = sys.stdin.readline

INF = 10**9

def solve():
    N = int(input().strip())
    M = int(input().strip())

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

    for i in range(1, N+1):
        for j in range(1, N+1):
            print(dist[i][j] if dist[i][j] != INF else 0, end=' ')
        print()
    return


solve()






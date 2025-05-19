import sys
input = sys.stdin.readline

INF = 10**9

def solve():
    def trace(s, e, lst):
        if not mid[s][e]:
            lst.append(s)
            return
        trace(s, mid[s][e], lst)
        trace(mid[s][e], e, lst)



    N = int(input().strip())
    M = int(input().strip())

    dist = [[INF]*(N+1) for _ in range(N+1)]
    mid = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        dist[a][b] = min(dist[a][b], c)
    for i in range(1, N+1):
        dist[i][i] = 0

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    mid[i][j] = k

    for i in range(1, N+1):
        for j in range(1, N+1):
            print(dist[i][j] if dist[i][j] != INF else 0, end=' ')
        print()

    for i in range(1, N+1):
        for j in range(1, N+1):
            lst = []
            if i == j:
                print(0)
            elif dist[i][j] != INF:
                trace(i, j, lst)
                print(len(lst)+1, *lst, j)
            else:
                print(0)



solve()






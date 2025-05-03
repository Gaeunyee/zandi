import sys
input = sys.stdin.readline


def multiple(x, y, N, M, K):
    m = [[0]*K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for k in range(M):
                m[i][j] += x[i][k] * y[k][j]


    return m


N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))
R = multiple(A, B, N, M, K)
for i in range(N):
    print(*R[i])

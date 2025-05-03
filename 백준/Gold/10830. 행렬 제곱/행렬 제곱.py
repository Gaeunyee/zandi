import sys
input = sys.stdin.readline
mod = 1000

def multiple(x, y, n):
    m = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m[i][j] += x[i][k] * y[k][j]
            m[i][j] %= mod

    return m


N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
R = [[0]*N for _ in range(N)]
for i in range(N):
    R[i][i] = 1
B = bin(B)[2:]

for i in range(len(B)-1, -1, -1):
    if B[i] == '1':
        R = multiple(A, R, N)
    A = multiple(A, A, N)

for i in range(N):
    print(*R[i])

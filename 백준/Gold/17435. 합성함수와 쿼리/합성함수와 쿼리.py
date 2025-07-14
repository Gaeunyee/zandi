import sys
input = sys.stdin.readline

LOG = 19
N = int(input().strip())
parent = [[0] * LOG for _ in range(N + 1)]

c = 1
for i in map(int, input().split()):
    parent[c][0] = i
    c += 1


def setPar():
    for j in range(1, LOG):
        for i in range(1, N + 1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]


def find(x, d):
    for i in range(LOG - 1, -1, -1):
        if d >= 1 << i:
            x = parent[x][i]
            d -= 1 << i
    return x


setPar()
Q = int(input())
for _ in range(Q):
    n, x = map(int, input().split())
    print(find(x, n))



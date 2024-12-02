import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
LOG = 20
N = int(input().strip())
tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
depth = [-1]*(N+1)
depth[0], depth[1] = -1, 0

parent = [[0]*LOG for _ in range(N+1)]


def dfs(n, d):
    for next in tree[n]:
        if depth[next] == -1:
            parent[next][0] = n
            depth[next] = d+1
            dfs(next, d+1)


def setPar():
    dfs(1, 0)
    for j in range(1, LOG):
        for i in range(1, N+1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]


def LCA(x, y): # x < y
    if depth[x] > depth[y]:
        x, y = y, x
    d = 0
    for i in range(LOG-1, -1, -1):
        if depth[y] - depth[x] >= (1 << i):
            d += 1 << i
            y = parent[y][i]
    if x == y:
        return d
    for i in range(LOG-1, -1, -1):
        if parent[x][i] != parent[y][i]:
            d += (1 << (i+1))
            x = parent[x][i]
            y = parent[y][i]
    return d + 2


def find(x, d):
    for i in range(LOG-1, -1, -1):
        if d >= (1 << i):
            d -= 1 << i
            x = parent[x][i]
    return x


setPar()
M = int(input().strip())
for _ in range(M):
    a, b, c = map(int, input().split())
    x = LCA(a, b)
    if x % 2 == 0:
        mid = find(max(a, b, key=lambda k: depth[k]), x//2)
        if LCA(mid, c) == x//2:
            print(mid)
            continue
    y = LCA(b, c)
    if y % 2 == 0:
        mid = find(max(b, c, key=lambda k: depth[k]), y//2)
        if LCA(mid, a) == y//2:
            print(mid)
            continue
    z = LCA(c, a)
    if z % 2 == 0:
        mid = find(max(c, a, key=lambda k: depth[k]), z//2)
        if LCA(mid, b) == z//2:
            print(mid)
            continue
    print(-1)




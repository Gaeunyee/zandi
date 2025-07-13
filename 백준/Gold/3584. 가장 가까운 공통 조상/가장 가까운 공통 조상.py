import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def solve():
    LOG = 16
    N = int(input().strip())
    tree = [[] for _ in range(N+1)]
    par = [0]*(N+1)

    for i in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        par[b] = a

    for i in range(1, N+1):
        if not par[i]:
            R = i
            break
    depth = [-1]*(N+1)
    depth[0], depth[R] = -1, 0

    parent = [[0]*LOG for _ in range(N+1)]


    def dfs(n, d):
        for next in tree[n]:
            if depth[next] == -1:
                parent[next][0] = n
                depth[next] = d+1
                dfs(next, d+1)


    def setPar():
        dfs(R, 0)
        for j in range(1, LOG):
            for i in range(1, N+1):
                parent[i][j] = parent[parent[i][j - 1]][j - 1]


    def LCA(x, y): # x < y
        for i in range(LOG-1, -1, -1):
            if depth[y] - depth[x] >= 2**i:
                y = parent[y][i]
        if x == y:
            return x
        for i in range(LOG-1, -1, -1):
            if parent[x][i] != parent[y][i]:
                x = parent[x][i]
                y = parent[y][i]
        return parent[x][0]


    setPar()

    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        print(LCA(b, a))
    else:
        print(LCA(a, b))


T = int(input())
for _ in range(T):
    solve()



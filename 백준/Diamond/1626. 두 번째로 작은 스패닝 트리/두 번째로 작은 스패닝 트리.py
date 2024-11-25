import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
LOG = 17
def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def union(a, b):
    x, y = find(a), find(b)
    if x == y:
        return False
    else:
        par[x] = y
        return True

V, E = map(int, input().split())
tree = [[] for _ in range(V+1)]
edge = []
for i in range(E):
    a, b, d = map(int, input().split())
    edge.append((d, a, b))
edge.sort(reverse=True)
cnt = 0

depth = [-1]*(V+1)
max_length = [[0]*LOG for _ in range(V+1)]
sec_length = [[-1]*LOG for _ in range(V+1)]
depth[1] = 0
parent = [[0]*LOG for _ in range(V+1)]
par = [i for i in range(V+1)]
spare = []
size = 0
while edge:
    td, ta, tb = edge.pop()
    if union(ta, tb):
        cnt += 1
        size += td
        tree[ta].append((td, tb))
        tree[tb].append((td, ta))
    else:
        spare.append((td, ta, tb))

if cnt < V-1:
    print(-1)
    exit()

def dfs(n, d):
    for l, next in tree[n]:
        if depth[next] == -1:
            parent[next][0] = n
            depth[next] = d+1
            max_length[next][0] = l
            dfs(next, d+1)


def setPar():
    dfs(1, 0)
    for j in range(1, LOG):
        for i in range(1, V+1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]
            max_length[i][j] = max(max_length[i][j - 1],
                                   max_length[parent[i][j - 1]][j - 1])

            if max_length[i][j] > max_length[parent[i][j - 1]][j - 1]:
                sec_length[i][j] = max(sec_length[i][j], max_length[parent[i][j - 1]][j - 1])
            elif max_length[i][j] > max_length[i][j - 1]:
                sec_length[i][j] = max(sec_length[i][j], max_length[i][j - 1])

            if max_length[i][j] > sec_length[parent[i][j - 1]][j - 1]:
                sec_length[i][j] = max(sec_length[i][j], sec_length[parent[i][j - 1]][j - 1])
            elif max_length[i][j] > sec_length[i][j - 1]:
                sec_length[i][j] = max(sec_length[i][j], sec_length[i][j - 1])


def LCA(x, y, d): # x < y
    max_ret = -1
    for i in range(LOG-1, -1, -1):
        if depth[y] - depth[x] >= 1 << i:
            if d == max_length[y][i]:
                max_ret = max(max_ret, sec_length[y][i])
            else:
                max_ret = max(max_ret, max_length[y][i])
            y = parent[y][i]
    if x == y:
        return max_ret
    for i in range(LOG-1, -1, -1):
        if parent[x][i] != parent[y][i]:
            if d == max_length[y][i]:
                max_ret = max(max_ret, sec_length[y][i])
            else:
                max_ret = max(max_ret, max_length[y][i])
            if d == max_length[x][i]:
                max_ret = max(max_ret, sec_length[x][i])
            else:
                max_ret = max(max_ret, max_length[x][i])
            x = parent[x][i]
            y = parent[y][i]
    if d == max_length[y][0]:
        max_ret = max(max_ret, sec_length[y][0])
    else:
        max_ret = max(max_ret, max_length[y][0])
    if d == max_length[x][0]:
        max_ret = max(max_ret, sec_length[x][0])
    else:
        max_ret = max(max_ret, max_length[x][0])
    return max_ret


setPar()
res = 10**6
for d, a, b in spare:
    if depth[a] > depth[b]:
        t = LCA(b, a, d)
        if t != -1:
            res = min(res, d-t)
    else:
        t = LCA(a, b, d)
        if t != -1:
            res = min(res, d-t)

if res != 10**6:
    print(size+res)
else:
    print(-1)

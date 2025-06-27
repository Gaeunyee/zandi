import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if par[x] < 0:
        return x
    t = find(par[x])
    offset[x] *= offset[par[x]]
    par[x] = t
    return par[x]


def union(a, b):
    global res
    x, y = find(a), find(b)
    if x != y:
        if x > y:
            x, y = y, x

        if isBip[x] != isBip[y]:
            res += par[x] if isBip[x] else par[y]

        par[x] += par[y]
        par[y] = x
        isBip[x] *= isBip[y]

        if offset[a] == offset[b]:
            offset[y] *= -1
        return True
    else:
        if offset[a] == offset[b]:
            if isBip[x]:
                res += par[x]
            isBip[x] = 0
            
        return False


N, Q = map(int, input().split())
offset = [1]*(N+1)
isBip = [1]*(N+1)
par = [-1]*(N+1)
res = 0
for _ in range(Q):
    u, v = map(int, input().split())
    union(u, v)
    print(-res)


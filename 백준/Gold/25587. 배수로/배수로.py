import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
par = [i for i in range(N+1)]
cap = [-1] + list(map(int, input().split()))
rain = [0] + list(map(int, input().split()))

ok = [(1 if rain[i] <= cap[i] else 0) for i in range(N+1)]
size = [1]*(N+1)
res = sum(ok)


def union(a, b):
    global res
    x, y = find(a), find(b)
    if x == y:
        return False
    if x > y:
        x, y = y, x
    par[x] = y
    rain[y] += rain[x]
    cap[y] += cap[x]
    if rain[y] > cap[y]:
        res -= size[x] if ok[x] else 0
        res -= size[y] if ok[y] else 0
        ok[y] = 0
    else:
        res += size[x] if not ok[x] else 0
        res += size[y] if not ok[y] else 0
        ok[y] = 1
    size[y] += size[x]



def find(a):
    if a == par[a]:
        return a
    else:
        par[a] = find(par[a])
        return par[a]

for _ in range(M):
    c, *u = map(int, input().split())
    if c == 1:
        union(u[0], u[1])
    else:
        print(N-res)


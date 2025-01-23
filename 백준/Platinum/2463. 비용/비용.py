import sys
m = 10**9
input = sys.stdin.readline

N, M = map(int, input().split())
hq = []
s = 0
for _ in range(M):
    u, v, w = map(int, input().split())
    s += w
    hq.append((-w, u, v))
res = 0
par = [i for i in range(N+1)]
size = [1]*(N+1)
cost = 0
hq.sort()
def find(a):
    if a == par[a]:
        return a
    par[a] = find(par[a])
    return par[a]


def union(a, b, w):
    global res, cost
    x, y = find(a), find(b)
    if x == y:
        cost += -w
        return False
    res = (res+(s-cost) * size[x] * size[y])%m
    cost += -w

    if x > y:
        par[x] = y
        size[y] += size[x]
    else:
        par[y] = x
        size[x] += size[y]
    return True


for w, u, v in hq:
    union(u, v, w)

print(res)


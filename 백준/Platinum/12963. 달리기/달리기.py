import sys
from collections import deque
input = sys.stdin.readline
mod = 10**9 + 7
N, M = map(int, input().split())
edge = []
w = 1
for _ in range(M):
    u, v = map(int, input().split())
    edge.append((w, u, v))
    w = (w*3) % mod

par = [i for i in range(N)]
def find(n):
    if n == par[n]:
        return n
    par[n] = find(par[n])
    return par[n]

def union(u, v):
    x, y = find(u), find(v)
    if x == y:
        return False
    else:
        if x > y:
            par[x] = y
        else:
            par[y] = x
    return True


res = 0
for w, u, v in reversed(edge):
    if (find(0) == find(u) and find(N-1) == find(v)) or (find(0) == find(v) and find(N-1) == find(u)):
        res = (res+w) % mod
    else:
        union(u, v)
print(res)
import sys

input = sys.stdin.readline

INF = 10**9

def solve():
    def find(a):
        if par[a] == a:
            return a
        par[a] = find(par[a])
        return par[a]

    def union(a, b):
        x, y = find(a), find(b)
        if x == y:
            return 0
        if x > y:
            x, y = y, x
        par[y] = x
        return 1

    M, N = map(int, input().split())
    if N == M == 0:
        return 0
    par = [i for i in range(N+1)]
    edge = []
    s = 0
    for _ in range(N):
        x, y, z = map(int, input().split())
        edge.append((z, x, y))
        s += z

    edge.sort()
    res = 0
    cnt = 0
    for d, a, b in edge:
        if cnt >= M-1:
            break
        if union(a, b):
            cnt += 1
            res += d

    print(s-res)
    return 1


while True:
    if not solve():
        break


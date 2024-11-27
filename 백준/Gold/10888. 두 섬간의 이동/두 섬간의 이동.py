import sys
input = sys.stdin.readline
INF = 10**6
N = int(input().strip())
par = [i for i in range(N+1)]
size = [1]*(N+1)
cnt, d = 0, 0
def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


def union(a, b):
    global cnt, d
    x = find(a)
    y = find(b)
    if x == y:
        return False
    else:
        cnt += size[x] * size[y]
        d += (size[x]*size[y]*(size[y]+1))//2 + ((size[x]-1)*size[x]*size[y])//2
        if x > y:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
        return True

for _ in range(N-1):
    t = int(input().strip())
    union(t, t+1)
    print(cnt, d)

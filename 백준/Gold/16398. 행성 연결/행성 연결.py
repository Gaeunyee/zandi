import sys
input = sys.stdin.readline

N = int(input())
edge = []
for i in range(N):
    t = list(map(int, input().split()))
    for j in range(i, N):
        edge.append((t[j], i, j))

par = [i for i in range(N+1)]
def find(x):
    if x == par[x]:
        return x
    par[x] = find(par[x])
    return par[x]

def union(a, b):
    x, y = find(a), find(b)
    if x == y:
        return False
    if x > y:
        x, y = y, x
    par[x] = y
    return True

edge.sort()
c = 0
res = 0
for d, i, j in edge:
    if c == N-1:
        break
    if union(i, j):
        res += d
        c += 1
print(res)


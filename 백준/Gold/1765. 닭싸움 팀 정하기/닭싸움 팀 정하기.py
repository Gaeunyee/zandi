import sys
from collections import deque
input = sys.stdin.readline


N = int(input().strip())
M = int(input().strip())
par = [i for i in range(N + 1)]
F = [[] for _ in range(N + 1)]
E = [[] for _ in range(N + 1)]
for _ in range(M):
    c, u, v = input().split()
    u, v = int(u), int(v)
    if c == 'F':
        F[u].append(v)
        F[v].append(u)
    else:
        E[u].append(v)
        E[v].append(u)


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


visited = [0]*(N+1)
for i in range(1, N+1):
    if visited[i]:
        continue
    qu = deque()
    qu.append(i)
    visited[i] = 1
    while qu:
        t = qu.popleft()
        for n in F[t]:
            if not visited[n]:
                union(t, n)
                qu.append(n)
                visited[n] = 1


visited = [0]*(N+1)

def dfs(t):
    f[visited[t]].append(t)
    for n in E[t]:
        if not visited[n]:
            visited[n] = visited[t]*(-1)
            dfs(n)


for i in range(1, N+1):
    if visited[i]:
        continue
    visited[i] = 1
    f = [[], [], []]
    dfs(i)
    for j in f[1]:
        union(i, j)
    for j in f[-1]:
        union(f[-1][0], j)


ok = [0]*(N+1)
res = 0
for i in range(1, N+1):
    if not ok[find(i)]:
        ok[par[i]] = 1
        res += 1

print(res)


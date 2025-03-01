import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+3)]
mento = [0]*(N+1)

arr = [-1]+list(map(int, input().split()))
for i in range(1, N+1):
    graph[arr[i]].append(i)
    mento[i] = arr[i]

par = [1]*(N+1)
def dfs(t, p):
    if isSep[t]:
        p = t
    par[t] = p
    for n in graph[t]:
        dfs(n, p)

def union(a, b):
    global res
    x, y = find(a), find(b)
    if x == y:
        return False
    if x > y:
        x, y = y, x
    par[x] = y
    return True



def find(a):
    if a == par[a]:
        return a
    else:
        par[a] = find(par[a])
        return par[a]

r = [0]
isSep = [0]*(N+1)
for _ in range(M):
    n = int(input().strip())
    isSep[n] += 1
    r.append(n)

for i in graph[-1]:
    dfs(i, i)
query = []
for i in range(K):
    query.append((i,)+tuple(map(int, input().split())))
query.sort(key=lambda x: x[1], reverse=True)
res = [0]*K
tmp = M
for i, a, b, c in query:
    while tmp > a:
        if mento[r[tmp]] != -1:
            isSep[r[tmp]] -= 1
            if isSep[r[tmp]] == 0:
                union(r[tmp], mento[r[tmp]])
        tmp -= 1

    if find(b) == find(c):
        res[i] = 1

for i in res:
    if i:
        print('Same Same;')
    else:
        print('No;')

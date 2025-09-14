import sys
sys.setrecursionlimit(10**5+7)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
deg = [0]*(N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
d = 0
dp = [0]*(N+1)
par = [0]*(N+1)
def dfs(t):
    for i in graph[t]:
        if dp[i] == 0 and i != 1:
            par[i] = t
            deg[t] += 1
            dp[i] = dp[t]+1
            dfs(i)
dfs(1)
l = list(map(int, input().split()))
p = []
for i in l:
    if deg[i]:
        p.append(i)
f = 1
t_node = 0
t_deg = 1
pt = -1
for i in l:
    if dp[i] == d+1:
        d += 1
    elif dp[i] < d:
        f = 0
        break
    if t_node != par[i]:
        if par[i] == p[pt+1]:
            pt += 1
        else:
            f = 0
            break
        if t_deg:
            f = 0
            break
        else:
            t_node = par[i]
            t_deg = deg[par[i]]-1
    else:
        t_deg -= 1

print(f)






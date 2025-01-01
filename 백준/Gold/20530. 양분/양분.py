import sys
input = sys.stdin.readline
sys.setrecursionlimit((10**5) * 2)

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1]*(N+1)
parent = [-1]*(N+1)
isCycle = [False]*(N+1)
area = [-1]*(N+1)

def dfs(par, n):
    visited[n] = 1
    parent[n] = par
    for nxt in graph[n]:
        if visited[nxt] == -1:
            if dfs(n, nxt):
                return True
        elif par != nxt and visited[nxt] == 1:
            isCycle[nxt] = True
            cur = n
            while cur != nxt:
                isCycle[cur] = True
                cur = parent[cur]
            return True
    return False

dfs(0, 1)
id = 2
def re_dfs(n):
    global id
    area[n] = id
    for nxt in graph[n]:
        if area[nxt] == -1 and not isCycle[nxt]:
            re_dfs(nxt)



for i in range(1, N+1):
    if isCycle[i]:
        re_dfs(i)
        id += 1

for _ in range(Q):
    a, b = map(int, input().split())
    if area[a] != area[b]:
        print(2)
    else:
        print(1)

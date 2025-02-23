import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input().strip())
par = [0, 0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
visited = [1] + [0]*N
for i in range(2, N+1):
    graph[par[i]].append(i)
e, o = 0, 0
def dfs(t, d):
    global e, o
    for i in graph[t]:
        dfs(i, d+1)
    if d % 2 == 0:
        e += 1
    else:
        o += 1


dfs(1, 0)
print(max(e, o))



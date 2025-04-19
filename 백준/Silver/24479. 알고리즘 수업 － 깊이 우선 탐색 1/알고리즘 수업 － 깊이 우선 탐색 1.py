import sys
sys.setrecursionlimit(10**5+7)
input = sys.stdin.readline


N, M, R = map(int, input().split())
visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

counter = 0


def dfs(node):
    global counter
    counter += 1
    visited[node] = counter
    for nxt in sorted(graph[node]):
        if visited[nxt] == 0:
            dfs(nxt)


dfs(R)
for i in visited[1:]:
    print(i)
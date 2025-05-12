import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

T = int(input().strip())

def dfs(c, t):
    visited[t] = c
    for nxt in graph[t]:
        if not visited[nxt]:
            if not dfs(-1*c, nxt):
                return False
        elif visited[nxt] == c:
            return False
    return True

for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [0]*(V+1)
    f = 1
    for i in range(1, V+1):
        if not visited[i]:
            if not dfs(1, i):
                f = 0
                break
    print("YES" if f else "NO")



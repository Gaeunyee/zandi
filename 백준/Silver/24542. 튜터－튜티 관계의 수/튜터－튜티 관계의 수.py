import sys
from collections import deque
input = sys.stdin.readline
mod = 10**9 + 7

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(N+1)
def bfs(s):
    visited[s] = 1
    cnt = 1
    qu = deque()
    qu.append(s)
    while qu:
        t = qu.popleft()
        for n in graph[t]:
            if not visited[n]:
                qu.append(n)
                visited[n] = 1
                cnt += 1
    return cnt

res = 1
for i in range(1, N+1):
    if not visited[i]:
        res *= bfs(i)
        res %= mod

print(res)



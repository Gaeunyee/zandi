import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N, M = map(int, input().split())
degree = [[] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
isOk = [False]*(N+1)
for _ in range(M):
    l = tuple(map(int, input().split()))
    t = l[-1]
    id = len(degree[t])
    degree[t].append(l[0])
    for i in l[1:-1]:
        graph[i].append((l[-1], id))
L = int(input().strip())
res = 0
qu = deque()

for j in map(int, input().split()):
    isOk[j] = True
    qu.append(j)
    res += 1


while qu:
    t = qu.popleft()
    for n, id in graph[t]:
        degree[n][id] -= 1
        if not isOk[n] and degree[n][id] <= 0:
            res += 1
            qu.append(n)
            isOk[n] = True

print(res)
for i in range(1, N+1):
    if isOk[i]:
        print(i, end=' ')



import sys
from collections import deque
input = sys.stdin.readline


N = int(input().strip())
visited = [0]*(N+1)
par = [0]*(N+2)
qu = deque()
visited[1] = 1
qu.append(1)
while qu:
    t = qu.popleft()
    n = [t+1, t*2, t*3]
    for i in n:
        if i <= N and not visited[i]:
            visited[i] = 1
            par[i] = t
            qu.append(i)
res = []
tr = N
while tr:
    res.append(tr)
    tr = par[tr]
print(len(res)-1)
print(*res)


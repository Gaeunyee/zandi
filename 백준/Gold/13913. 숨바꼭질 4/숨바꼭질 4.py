import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())

if K <= N:
    print(N-K)
    print(*range(N, K-1, -1))

else:
    size = K*2+1
    visited = [-1]*size
    par = [-1]*size
    qu = deque()
    visited[N] = 0
    qu.append(N)
    while qu:
        t = qu.popleft()
        for nxt in (t-1, t+1, t*2):
            if 0 <= nxt < size and visited[nxt] == -1:
                visited[nxt] = visited[t]+1
                par[nxt] = t
                if nxt == K:
                    break
                qu.append(nxt)
    print(visited[K])
    tr = K
    res = []
    while tr != -1:
        res.append(tr)
        tr = par[tr]
    print(*res[::-1])


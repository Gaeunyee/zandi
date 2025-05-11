import sys
from collections import deque
input = sys.stdin.readline

INF = 10**9 + 7
size = 10**6 + 1
def solve():
    N, M = map(int, input().split())
    visited = [INF]*101
    warp = [0]*101
    for _ in range(N+M):
        a, b = map(int, input().split())
        warp[a] = b
    qu = deque()
    qu.append(1)
    visited[0] = 1
    visited[1] = 0
    while qu and visited[100] == INF:
        t = qu.popleft()
        for n in range(t+1, min(101, t+7)):
            if visited[n] == INF:
                visited[n] = visited[t]+1
                if warp[n] != 0:
                    tr = n
                    f = 1
                    while warp[tr] != 0:
                        if visited[warp[tr]] <= visited[t] + 1:
                            f = 0
                            break
                        visited[warp[tr]] = visited[t] + 1
                        tr = warp[tr]
                    if f:
                        qu.append(tr)
                else:
                    qu.append(n)

    print(visited[100])


solve()


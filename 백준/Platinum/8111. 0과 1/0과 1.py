import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())

def solve(N):
    if N == 1:
        return 1
    visited = [[0]*N for _ in range(101)]
    visited[1][1] = 1
    qu = deque()
    qu.append((1, 1))
    while qu:
        l, r = qu.popleft()
        if r == 0:
            return visited[l][r]
        nxt = [(r*10) % N, (r*10+1) % N]
        for i in range(2):
            n = nxt[i]
            if not visited[l+1][n]:
                visited[l+1][n] = visited[l][r]*10 + i
                qu.append((l+1, n))
    return -1

for _ in range(T):
    res = solve(int(input().strip()))
    if res == -1:
        print("BRAK")
    else:
        print(res)


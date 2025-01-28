import sys
from collections import deque
input = sys.stdin.readline
INF = 10**9+7


N, M = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(tuple(map(int, input().split())))

start, end = map(int, input().split())
visited = [(0, 0)]*(N+1)
used = [0]*(M+1)
qu = deque()
qu.append((0, start))
visited[start] = (-1, -1)
while qu:
    att, h = qu.popleft()
    if h == end:
        print(att)
        t, el = visited[end]
        res = []
        while t != -1:
            res.append(el+1)
            t, el = visited[t]
        while res:
            print(res.pop())
        exit()
    for k in range(M):
        if not used[k]:
            x, y = arr[k]
            if (h-x) >= 0 and (h-x) % y == 0:
                used[k] = 1
                c = x
                while c <= N:
                    if visited[c] == (0, 0):
                        qu.append((att+1, c))
                        visited[c] = (h, k)
                    c += y
print(-1)


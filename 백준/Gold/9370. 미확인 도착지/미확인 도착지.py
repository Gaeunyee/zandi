import sys
from heapq import *
input = sys.stdin.readline
INF = 10**9

T = int(input().strip())
def solve():
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    table = [INF] * (n + 1)
    table[s] = 0
    used = [0] * (n + 1)
    qu = []
    heappush(qu, (0, s))
    while qu:
        d, tmp = heappop(qu)
        if table[tmp] < d:
            continue
        for nxt, w in graph[tmp]:
            if d + w == table[nxt]:
                used[nxt] = max(used[nxt], used[tmp])
                if (g, h) == (tmp, nxt) or (g, h) == (nxt, tmp):
                    used[nxt] = 1
            elif d + w < table[nxt]:
                used[nxt] = used[tmp]
                if (g, h) == (tmp, nxt) or (g, h) == (nxt, tmp):
                    used[nxt] = 1
                table[nxt] = d + w
                qu.append((table[nxt], nxt))

    for _ in range(t):
        used[int(input().strip())] *= -1
    for i in range(1, n + 1):
        if used[i] < 0:
            print(i, end=' ')
    print()
for _ in range(T):
    solve()



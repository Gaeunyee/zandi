import sys
from heapq import *
input = sys.stdin.readline


N = int(input())
table = []
for _ in range(N):
    a, b = map(int, input().split())
    table.append((a, b))

table.sort()
hq = []
heappush(hq, table[0][1])
res = 1
for st, ed in table[1:]:
    if hq[0] > st:
        heappush(hq, ed)
        res += 1
    else:
        heappop(hq)
        heappush(hq, ed)

print(res)


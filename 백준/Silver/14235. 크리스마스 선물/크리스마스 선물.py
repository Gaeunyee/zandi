import sys
from heapq import *
input = sys.stdin.readline


n = int(input().strip())
hq = []
for _ in range(n):
    a, *s = map(int, input().split())
    if a == 0:
        if hq:
            print(-heappop(hq))
        else:
            print(-1)
    else:
        for i in s:
            heappush(hq, -i)




import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input().strip())
lq, rq = [], []
pivot = -1
for i in range(1, N+1):
    t = int(input().strip())
    if i == 1:
        pivot = t
    elif i % 2 == 1:
        if t <= pivot:
            heappush(lq, -t)
        else:
            heappush(rq, t)
            heappush(lq, -pivot)
            pivot = heappop(rq)
    elif i % 2 == 0:
        if t > pivot:
            heappush(rq, t)
        else:
            heappush(rq, pivot)
            heappush(lq, -t)
            pivot = -heappop(lq)
    print(pivot)

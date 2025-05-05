import sys
from heapq import *
input = sys.stdin.readline


N = int(input().strip())
hq = []
for _ in range(N):
    for i in map(int, input().split()):
        heappush(hq, i)
    while len(hq) > N:
        heappop(hq)

print(hq[0])


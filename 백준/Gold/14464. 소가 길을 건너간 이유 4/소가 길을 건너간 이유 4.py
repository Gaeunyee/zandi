import sys
from heapq import *
input = sys.stdin.readline


C, N = map(int, input().split())
chicken = []
for _ in range(C):
    chicken.append(int(input().strip()))

cow = []
for _ in range(N):
    cow.append(tuple(map(int, input().split())))

cow.sort()
chicken.sort()
cow.append((10**9 + 7, 10**9 + 7))
qu = []
p = 0
res = 0
for i in chicken:
    while cow[p][0] <= i:
        heappush(qu, cow[p][1])
        p += 1
    while qu and qu[0] < i:
        heappop(qu)
    if qu:
        heappop(qu)
        res += 1

print(res)


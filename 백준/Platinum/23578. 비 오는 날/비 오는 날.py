import sys
from heapq import *
input = sys.stdin.readline

N = int(input().strip())
deg = [1]*(N+1)
qu = []
lst = list(map(int, input().split()))
for i in range(len(lst)):
    heappush(qu, (3*lst[i], i))
cnt = N
res = sum(lst)
if N == 1:
    print(0)
    quit()
while cnt < 2*(N-1):
    t, idx = heappop(qu)
    res += t
    cnt += 1
    deg[idx] += 1
    heappush(qu, ((2*deg[idx]+1)*lst[idx], idx))

print(res)
# N, M = map(int, input().split())



import sys
import heapq as hq
input = sys.stdin.readline


#sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
b = []
for _ in range(N):
    m, v = map(int, input().split())
    b.append((m, v))
bag = []
for _ in range(K):
    bag.append(int(input().strip()))

bag.sort()
b.sort()
res = 0
idx = 0
pq = []
for i in bag:
    while idx < N and b[idx][0] <= i:
        hq.heappush(pq, (-b[idx][1], b[idx][0]))
        idx += 1
    if pq:
        v, w = hq.heappop(pq)
        res -= v

print(res)



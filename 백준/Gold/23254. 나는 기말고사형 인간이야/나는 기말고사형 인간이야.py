import sys
from heapq import *
input = sys.stdin.readline


N, M = map(int, input().split())
score = list(map(int, input().split()))
ef = list(map(int, input().split()))
hq = []
for i in range(M):
    heappush(hq, (-min(100-score[i], ef[i]), i))
N *= 24
while N:
    d, idx = heappop(hq)
    if d == 0:
        break
    r = 100-score[idx]
    k = min(N, r//(-d))
    score[idx] += k*(-d)
    N -= k

    heappush(hq, (-(100-score[idx]), idx))

print(sum(score))


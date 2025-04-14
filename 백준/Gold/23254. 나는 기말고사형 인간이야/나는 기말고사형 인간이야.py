import sys
from heapq import *
input = sys.stdin.readline


N, M = map(int, input().split())
score = list(map(int, input().split()))
ef = list(map(int, input().split()))
hq = []
for i in range(M):
    heappush(hq, (-min(100-score[i], ef[i]), i))

for i in range(N*24):
    d, idx = hq[0]
    score[idx] -= d
    if 100-score[idx] < -d:
        heappop(hq)
        heappush(hq, (-(100-score[idx]), idx))

print(sum(score))


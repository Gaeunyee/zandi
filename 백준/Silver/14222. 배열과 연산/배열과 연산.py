import sys
from collections import deque
from heapq import *
input = sys.stdin.readline

INF = 10**9

N, K = map(int, input().split())
lst = list(map(int, input().split()))
cnt = [0]*(N+1)
for i in lst:
    if i <= N:
        cnt[i] += 1

f = 1
for i in range(1, N+1):
    if cnt[i] == 0:
        f = 0
        break
    elif cnt[i] > 1:
        if i+K <= N:
            cnt[i+K] += cnt[i]-1

print(f)

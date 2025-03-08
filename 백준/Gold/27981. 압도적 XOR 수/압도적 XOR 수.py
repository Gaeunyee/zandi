import sys
from math import ceil, log
input = sys.stdin.readline
SIZE = 10**7

N, K = map(int, input().split())
c = N
size = int(log(N, 2))+1
box = [1 << i for i in range(size)]
remain = []
for i in range(size):
    remain.append(min(c, 1<<i))
    c -= min(c, 1<<i)

for i in range(size):
    for k in range(1, K):
        remain[i] -= min(remain[i], box[i]//2)
        box[i] -= box[i] // 2
print(sum(remain))


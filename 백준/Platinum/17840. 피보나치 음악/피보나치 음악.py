import sys
from heapq import *
input = sys.stdin.readline


Q, M = map(int, input().split())


count = ['c']*(10**4)
count[0], count[1], count[2] = '0', '1', '1'
a, b = 1, 1
end = -1
idx = 3
for i in range(3, 10**4):
    c = (a+b) % M
    for s in str(c):
        count[idx] = s
        idx += 1
    if c == 1 and b == 0:
        end = idx-2
        break
    a = b
    b = c

for _ in range(Q):
    N = int(input().strip())
    print(count[N % end])


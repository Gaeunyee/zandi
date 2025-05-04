import sys
from bisect import *
input = sys.stdin.readline


N, C = map(int, input().split())

home = []
for _ in range(N):
    home.append(int(input().strip()))
home.sort()
l, r = 0, 10**9 + 7

while l + 1 < r:
    m = (l+r)//2
    c, t = 1, 0
    flag = 1
    while t != N-1 and c < C:
        t = bisect_left(home, home[t]+m)
        if t == N:
            flag = 0
            break
        c += 1
    if not flag or c < C:
        r = m
    else:
        l = m

print(l)




import sys
from bisect import *
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
A, B = map(int, input().split())
lst.sort()
res = -1
I = -1

for i in range(1, N):
    t = (lst[i] + lst[i - 1]) // 2
    if t % 2 == 0:
        if t > A:
            t -= 1
        elif t < B:
            t += 1
    if A <= t <= B:
        if res < min(abs(lst[i]-t), abs(t-lst[i-1])):
            res = min(abs(lst[i]-t), abs(t-lst[i-1]))
            I = t

A += 1 if A%2 == 0 else 0
B -= 1 if B%2 == 0 else 0
k = bisect_left(lst, A)
if k == N:
    d = abs(lst[k - 1] - A)
elif k == 0:
    d = abs(lst[k] - A)
else:
    d = min(abs(A - lst[k - 1]), abs(lst[k] - A))
if res < d:
    res = d
    I = A

k = bisect_right(lst, B)
if k == N:
    d = abs(lst[k - 1] - B)
elif k == 0:
    d = abs(lst[k] - B)
else:
    d = min(abs(B - lst[k - 1]), abs(lst[k] - B))
if res < d:
    res = d
    I = B


print(I)
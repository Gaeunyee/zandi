import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
INF = 10 ** 6
size = 97

L, N, K = map(int, input().split())
l, r = 0, L
charge = list(map(int, input().split()))
charge.append(L)

while l+1 < r:
    m = (l+r)//2
    cnt = K
    b = m
    tmp = 0
    ok = 1
    for i in charge:
        if i-tmp > b:
            if cnt and i-tmp <= m:
                cnt -= 1
                b = m
            else:
                ok = 0
                break
        b -= i-tmp
        tmp = i
    if ok:
        r = m
    else:
        l = m


print(r)




import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
INF = 10 ** 6
size = 97


T = int(input().strip())
for _ in range(T):
    n, s = map(int, input().split())
    seat = list(map(int, input().split()))
    seat.sort()
    l, r = 0, 10**9+7
    while l+1 < r:
        m = (l+r)//2
        st = seat[0]
        cnt = 1
        for i in seat[1:]:
            if i-st < m:
                continue
            st = i
            cnt += 1
        if cnt >= s:
            l = m
        else:
            r = m
    print(l)






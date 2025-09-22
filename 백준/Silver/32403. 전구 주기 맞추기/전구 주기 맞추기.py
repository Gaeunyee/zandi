import sys
from collections import deque
input = sys.stdin.readline





def solve():
    N, T = map(int, input().split())
    lst = list(map(int, input().split()))
    l = []
    for i in range(1, T+1):
        if T%i == 0:
            l.append(i)
    res = 0
    for i in lst:
        t = 10**9
        for j in l:
            t = min(t, abs(i-j))
        res += t
    print(res)


solve()


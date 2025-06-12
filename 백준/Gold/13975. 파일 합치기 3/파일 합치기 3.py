import sys
from heapq import *
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    lst = list(map(int, input().split()))
    heapify(lst)
    res = 0
    for _ in range(N-1):
        t = 0
        t += heappop(lst)
        t += heappop(lst)
        heappush(lst, t)
        res += t
    print(res)


T = int(input().strip())
for _ in range(T):
    solve()


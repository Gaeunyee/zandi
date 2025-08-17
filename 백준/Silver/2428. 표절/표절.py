import sys
from bisect import *
input = sys.stdin.readline
INF = 10**6

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = 0
for i in range(N):
    res += i-bisect_left(lst, lst[i]*0.9)
print(res)

import sys
input = sys.stdin.readline


A, B, V = map(int, input().split())
l, r = 0, 10**9 + 3

while l+1 < r:
    m = (l+r)//2
    d = (A-B)*(m-1) + A
    if d >= V:
        r = m
    else:
        l = m

print(r)


import sys
input = sys.stdin.readline

N = int(input().strip())
k = int(input().strip())
l, r = 1, k
while l+1 < r:
    m = (l+r)//2
    t = 0
    for i in range(1, N+1):
        t += min(N, m//i)
    if t >= k:
        r = m
    else:
        l = m

print(r)

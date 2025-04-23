import sys
input = sys.stdin.readline


N = int(input().strip())
l, r = 0, 10**5
while l+1 < r:
    m = (l+r)//2
    if m*(m+1)//2 >= N:
        r = m
    else:
        l = m

if r % 2 == 0:
    d = (r*(r+1)//2)-N
    x, y = r-d, 1+d
else:
    d = (r*(r+1)//2)-N
    x, y = 1+d, r-d

print(f'{x}/{y}')
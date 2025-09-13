import sys
input = sys.stdin.readline

m, s = 1000, 0
for _ in range(7):
    N = int(input())
    if N % 2 == 1:
        m = min(m, N)
        s += N

if m == 1000:
    print(-1)
else:
    print(s)
    print(m)
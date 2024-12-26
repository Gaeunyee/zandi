import sys

INF = 10**7+7
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
size = N//2
a, b = arr[:size], arr[size:]
c1 = []
for i in range(1 << size):
    mask = 0
    s = 0
    while mask < size:
        if i & (1 << mask):
            s += a[mask]
        mask += 1
    c1.append(s)
c2 = []
for i in range(1 << (N-size)):
    mask = 0
    s = 0
    while mask < (N-size):
        if i & (1 << mask):
            s += b[mask]
        mask += 1
    c2.append(s)

c1.sort(reverse=True)
c2.sort()
c2.append(10**9+7)
r = 0
res = 0
for l in c1:
    while True:
        if l+c2[r] <= M:
            r += 1
        else:
            break
    res += r
print(res)



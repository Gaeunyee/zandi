import sys

INF = 10**7+7
input = sys.stdin.readline


N = int(input().strip())
arr = []

for _ in range(N):
    b, h, w, d = map(int, input().split())
    arr.append((b, h, w*d))
V = int(input().strip())
def makeNum(t):
    ret = 0
    for b, h, a in arr:
        if t > b:
            ret += min(t-b, h)*a
    return ret


if V == 0:
    print(0.00)
else:
    l, r = 0, 10**6+40000
    while r-l > 0.001:
        mid = (l+r)/2
        if makeNum(mid) >= V:
            r = mid
        else:
            l = mid
    if r == 10**6+40000:
        print("OVERFLOW")
    else:
        print(round(r, 2))



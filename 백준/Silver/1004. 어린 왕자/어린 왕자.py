import sys
input = sys.stdin.readline



def isIn(x, y, a ,b, r):
    if (x-a)**2 + (y-b)**2 > r**2:
        return 0
    return 1

T = int(input())

for _ in range(T):
    sx, sy, ex, ey = map(int, input().split())
    N = int(input())
    ok = [0]*N
    for i in range(N):
        a, b, r = map(int, input().split())
        ok[i] = isIn(sx, sy, a, b, r) ^ isIn(ex, ey, a, b, r)

    print(sum(ok))

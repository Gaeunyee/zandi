import sys

INF = 10**7+7
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))

def makeNum(t):
    ret = 0
    for i in arr:
        ret += t//i + 1
    return ret


if N <= M:
    print(N)
else:
    l, r = 0, 30*((N//M)+1)
    while l+1 < r:
        mid = (l+r)//2
        if makeNum(mid) >= N:
            r = mid
        else:
            l = mid
    c = N-makeNum(l)
    for i in range(M):
        if r % arr[i] == 0:
            c -= 1
            if c == 0:
                print(i+1)
                break


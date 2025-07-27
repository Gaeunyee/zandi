import sys
input = sys.stdin.readline

size = 30
mod = 10**9 + 7
N = int(input())
lst = [0]+list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    c, *x = map(int, input().split())
    if c == 1:
        t = x[1]
        for i in range(x[0], -1, -1):
            if x[1] == 0:
                break
            d = min(lst[i], x[1])
            lst[i] += d
            x[1] -= d
        for i in range(x[0]+1, N+1):
            if t == 0:
                break
            d = min(lst[i], t)
            lst[i] += d
            t -= d

    else:
        print(lst[x[0]])

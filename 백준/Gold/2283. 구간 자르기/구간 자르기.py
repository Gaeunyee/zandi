import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)


def solve():
    N, K = map(int, input().split())
    arr = [0] * (10 ** 6 + 1)

    for _ in range(N):
        a, b = map(int, input().split())
        arr[a] += 1
        arr[b] -= 1

    sarr = [0] * (10 ** 6 + 1)
    sarr[0] = arr[0]
    s, r = arr[0], 1
    p = arr[0]
    for i in range(1, 10 ** 6):
        p += arr[i]
        sarr[i] = p
    for l in range(10**6):
        while r <= 10**6 and s < K:
            s += sarr[r]
            r += 1
        if s == K:
            print(l, r)
            return
        s -= sarr[l]
    print(0, 0)

solve()

import sys
input = sys.stdin.readline


def solve():
    N, B, C = map(int, input().split())
    c1, c2 = B+C, B+2*C
    lst = list(map(int, input().split())) + [0, 0]
    cost = 0
    if C >= B:
        print(sum(lst)*B)
        exit()
    for i in range(N):
        if lst[i+1] > lst[i+2]:
            d = min(lst[i], lst[i+1]-lst[i+2])
            lst[i] -= d
            lst[i+1] -= d
            cost += d*c1
        d = min(lst[i], lst[i+1], lst[i+2])
        lst[i] -= d
        lst[i+1] -= d
        lst[i+2] -= d
        cost += d*c2 + lst[i]*B

    print(cost)

solve()

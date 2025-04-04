import sys
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    hole = [(-1, 0)]
    idx = 0
    for size in map(int, input().split()):
        if hole[-1][0] < size+idx:
            hole.append((size+idx, idx+1))
        idx += 1

    Q = int(input().strip())
    for i in map(int, input().split()):
        l, r = 0, len(hole)-1
        while l+1 < r:
            m = (l+r)//2
            if hole[m][0] >= i:
                r = m
            else:
                l = m
        print(hole[r][1])

solve()

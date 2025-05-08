import sys
input = sys.stdin.readline

INF = 10**9 + 7
size = 40001
def solve():
    N = int(input().strip())
    w = list(map(int, input().split()))
    M = int(input().strip())
    c = list(map(int, input().split()))
    dp = set()
    for i in w:
        tmp = set()
        for j in dp:
            if 0 < i+j < size:
                tmp.add(i+j)
            if 0 < i-j < size:
                tmp.add(i-j)
            if 0 < j-i < size:
                tmp.add(j-i)
        dp.add(i)
        dp |= tmp

    for i in c:
        print("Y" if i in dp else "N", end=' ')

solve()


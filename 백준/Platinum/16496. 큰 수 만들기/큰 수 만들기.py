import sys
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    lst = input().split()
    f = 0
    for i in lst:
        if i != '0':
            f = 1
    if not f:
        print(0)
        return
    lst.sort(key=lambda x: int(x)/(10**len(x)-1), reverse=True)
    for i in range(N):
        print(lst[i], end='')


solve()



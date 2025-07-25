import sys
from math import ceil, log
input = sys.stdin.readline

mod = 10**9 + 7


def edit(i, k):
    while i > 0:
        tree[i] += k
        i //= 2


def getSum(start, end):
    ret = 0
    while start <= end:
        if start % 2 == 1:
            ret += tree[start]
            start += 1
        if end % 2 == 0:
            ret += tree[end]
            end -= 1
        start, end = start//2, end//2
    return ret

T = 1
for _ in range(T):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(tuple(map(int, input().split())))
    lst.sort()
    r = [0]*(n+1)
    nlst = [(0, lst[0][1], 0)]
    x = 0
    for i in range(1, n):
        if lst[i-1][0] < lst[i][0]:
            x += 1
        nlst.append((x, lst[i][1], i))

    nlst.sort(key=lambda x: (-x[1], x[0]))

    H = ceil(log(n, 2))
    treeSize = pow(2, H+1)
    tree = [0]*(treeSize+1)
    startIndex = treeSize // 2

    for x, y, i in nlst:
        r[i] += getSum(startIndex + x + 1, startIndex + n-1)
        edit(startIndex+x, 1)

    nlst.sort(key=lambda x: (-x[1], -x[0]))

    H = ceil(log(n, 2))
    treeSize = pow(2, H + 1)
    tree = [0] * (treeSize + 1)
    startIndex = treeSize // 2

    res = 0
    for x, y, i in nlst:
        res = (res + r[i] * getSum(startIndex, startIndex + x - 1))%mod
        edit(startIndex + x, 1)

    print(res)

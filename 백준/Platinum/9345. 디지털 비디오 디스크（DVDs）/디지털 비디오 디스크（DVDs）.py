import sys
from math import ceil, log
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    H = ceil(log(N, 2))
    treeSize = pow(2, H+1)
    maxtree = [0]*(treeSize+1)
    mintree = [10**9]*(treeSize+1)
    startIndex = treeSize // 2
    for i in range(N):
        maxtree[startIndex+i] = i
        mintree[startIndex+i] = i

    def init(i):
        while i != 0:
            maxtree[i // 2] = max(maxtree[i // 2], maxtree[i])
            mintree[i // 2] = min(mintree[i // 2], mintree[i])
            i -= 1

    def edit(i, b):
        mintree[i], maxtree[i] = b, b
        i //= 2
        while i != 0:
            maxtree[i] = max(maxtree[i*2+1], maxtree[i*2])
            mintree[i] = min(mintree[i*2+1], mintree[i*2])
            i //= 2

    init(treeSize-1)

    def getSum(start, end):
        minint, maxint = 10**9, 0
        while start <= end:
            if start % 2 == 1:
                minint = min(mintree[start], minint)
                maxint = max(maxtree[start], maxint)
                start += 1
            if end % 2 == 0:
                minint = min(mintree[end], minint)
                maxint = max(maxtree[end], maxint)
                end -= 1
            start, end = start//2, end//2
        return minint, maxint


    for i in range(M):
        c, l, r = map(int, input().split())
        if c == 0:
            t = mintree[l+startIndex]
            edit(l+startIndex, mintree[r+startIndex])
            edit(r+startIndex, t)
        else:
            print('YES' if getSum(startIndex+l, startIndex+r) == (l, r) else 'NO')


T = int(input().strip())
for _ in range(T):
    solve()

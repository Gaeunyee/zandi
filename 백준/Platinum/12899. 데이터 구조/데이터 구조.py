import sys
from math import ceil, log
input = sys.stdin.readline

N = 10**6 * 2
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2 - 1




def editTree(i, new):
    while i != 0:
        tree[i] += new
        i //= 2


def getSum(start, end):
    res = 0
    while start <= end:
        if start % 2 == 1:
            res += tree[start]
            start += 1
        if end % 2 == 0:
            res += tree[end]
            end -= 1
        start, end = start//2, end//2
    return res


T = int(input().strip())
for _ in range(T):
    a, b = map(int, input().split())
    if a == 1:
        editTree(startIndex + b, 1)
    else:
        start, end = 1, 10**6 * 2
        while start < end:
            mid = (start+end)//2
            if getSum(startIndex + 1, startIndex + mid) < b:
                start = mid + 1
            else:
                end = mid
        editTree(startIndex + start, -1)
        print(start)

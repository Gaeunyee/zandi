import sys
from math import ceil, log
input = sys.stdin.readline


N, Q = map(int, input().split())
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


for _ in range(Q):
    c, a, b = map(int, input().split())
    if c == 1:
        editTree(startIndex + a, b)
    else:
        print(getSum(startIndex+a, startIndex+b))

import sys
from math import ceil, log
input = sys.stdin.readline

N = int(input().strip())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2




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


lst = list(map(int, input().split()))
lst = [(lst[i], i) for i in range(N)]
lst.sort(reverse=True)
res = 0
for s, i in lst:
    res += getSum(startIndex, startIndex+i)
    editTree(startIndex+i, 1)

print(res)

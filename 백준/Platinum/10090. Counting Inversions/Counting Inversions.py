import sys
from math import ceil, log
input = sys.stdin.readline

N = int(input().strip())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2 - 1
lst = list(map(int, input().split()))


def editTree(idx):
    while idx != 0:
        tree[idx] += 1
        idx //= 2
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

cnt = 0
for i in range(N-1, -1, -1):
    editTree(startIndex+lst[i])
    cnt += getSum(startIndex+1, startIndex+lst[i]-1)

print(cnt)
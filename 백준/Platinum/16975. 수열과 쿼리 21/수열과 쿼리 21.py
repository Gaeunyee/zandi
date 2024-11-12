import sys
from math import ceil, log
input = sys.stdin.readline

N = int(input().strip())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2 - 1
lst = [-1] + list(map(int, input().split()))

def setTree(i):
    while i != 0:
        tree[i//2] += tree[i]
        i -= 1

def getSum(i):
    res = lst[i - startIndex]
    while i != 0:
        res += tree[i]
        i //= 2
    return res


def setSum(start, end, k):
    while start <= end:
        if start % 2 == 1:
            tree[start] += k
            start += 1
        if end % 2 == 0:
            tree[end] += k
            end -= 1
        start, end = start//2, end//2


M = int(input().strip())
c1 = []
c2 = []
idx = 0
for _ in range(M):
    cmd, *arg = map(int, input().split())
    if cmd == 1:
        i, j, k = arg
        setSum(startIndex+i, startIndex+j, k)
    else:
        x = arg[0]
        print(getSum(startIndex+x))
import sys
from math import ceil, log
input = sys.stdin.readline

N = int(input().strip())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
c_tree = [0]*(treeSize+1)
startIndex = treeSize // 2 - 1
lst = [-1] + list(map(int, input().split()))


def getSum(i):
    res = lst[i - startIndex]
    size = 1
    k = 0
    while i != 0:
        res += tree[i] + k * c_tree[i]
        if i % 2 == 1:
            k += size
        size = size << 1
        i //= 2
    return res


def setSum(start, end, u, v):
    i, j = u, v
    size = 1
    while start <= end:
        if start % 2 == 1:
            c_tree[start] += 1
            tree[start] += i-u+1
            start += 1
            i += size
        if end % 2 == 0:
            c_tree[end] += 1
            tree[end] += ((j-size+1)-u+1)
            end -= 1
            j -= size
        start, end = start//2, end//2
        size = size << 1


Q = int(input().strip())
for _ in range(Q):
    cmd, *arg = map(int, input().split())
    if cmd == 1:
        i, j = arg
        setSum(startIndex+i, startIndex+j, i, j)
    else:
        print(getSum(startIndex+arg[0]))

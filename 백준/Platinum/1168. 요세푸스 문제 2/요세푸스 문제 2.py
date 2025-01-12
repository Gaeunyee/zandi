import sys
from math import ceil, log
input = sys.stdin.readline

N, K = map(int, input().split())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2 - 1
tree[startIndex+1:startIndex+1+N] = [1]*N
arrSize = 2**H
def setTree(i):
    while i != 0:
        tree[i//2] += tree[i]
        i -= 1

setTree(startIndex+N)

def editTree(i):
    while i != 0:
        tree[i] -= 1
        i //= 2


def getSum(start):
    cnt = 0
    idx, size = start-startIndex, 1
    while cnt < K:
        if start % 2 == 1:  # 오른쪽 자식
            if tree[start] + cnt <= K:
                cnt += tree[start]
                if idx + size > arrSize:
                    idx = 1
                else:
                    idx = idx + size
                size = 1
                start = startIndex + idx
        else:
            if tree[start//2] + cnt < K:
                start //= 2
                size *= 2
            else:
                cnt += tree[start]
                if idx + size > arrSize:
                    idx = 1
                else:
                    idx = idx + size
                size = 1
                start = startIndex + idx
    if idx != 1:
        return idx-1
    return 1


s = K
print('<', end='')
for i in range(N):
    if i != N-1:
        print(s, end=', ')
    else:
        print(s, end='')
        break
    editTree(startIndex+s)
    s = getSum(startIndex+s)
print('>')


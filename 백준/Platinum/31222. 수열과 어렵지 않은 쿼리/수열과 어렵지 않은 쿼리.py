import sys
from math import log, ceil
m = 10**9
input = sys.stdin.readline

N, Q = map(int, input().split())
H = ceil(log(N, 2))
treeSize = 2**(H+1)
startIndex = 2**H - 1

tree = [0]*treeSize
arr = [0]+list(map(int, input().split()))
arr[0] = arr[1]

tr = arr[1]
cnt = 1
for i in range(1, N+1):
    if arr[i] != tr:
        cnt += 1
        tr = arr[i]
    tree[startIndex+i] = cnt

def editSum(start, end, d):
    while start <= end:
        if start % 2 == 1:
            tree[start] += d
            start += 1
        if end % 2 == 0:
            tree[end] += d
            end -= 1
        start, end = start // 2, end // 2


def getSum(idx):
    ret = 0
    while idx != 0:
        ret += tree[idx]
        idx //= 2
    return ret

for _ in range(Q):
    c, a, b = map(int, input().split())
    if c == 1:
        arr[a] = b
        if a >= 2:
            if arr[a] != arr[a-1]:
                d = getSum(startIndex+a-1)+1 - getSum(startIndex+a)
                editSum(startIndex+a, startIndex+a, d)

            else:
                d = getSum(startIndex + a - 1) - getSum(startIndex + a)
                editSum(startIndex + a, startIndex + a, d)


        if a <= N-1:
            if arr[a] != arr[a+1]:
                d = getSum(startIndex+a)+1 - getSum(startIndex+a+1)
                editSum(startIndex+a+1, startIndex+N, d)
            else:
                d = getSum(startIndex + a) - getSum(startIndex + a + 1)
                editSum(startIndex + a + 1, startIndex + N, d)

    else:
        print(getSum(startIndex+b)-getSum(startIndex+a)+1)


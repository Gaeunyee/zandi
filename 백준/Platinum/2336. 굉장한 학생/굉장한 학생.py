import sys
from math import ceil, log
input = sys.stdin.readline

INF = 10**6
N = int(input().strip())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [INF]*(treeSize+1)
startIndex = treeSize // 2 - 1


def edit(i, k):
    while i > 0:
        tree[i] = min(tree[i], k)
        i //= 2


def getSum(start, end):
    ret = INF
    while start <= end:
        if start % 2 == 1:
            ret = min(ret, tree[start])
            start += 1
        if end % 2 == 0:
            ret = min(ret, tree[end])
            end -= 1
        start, end = start//2, end//2
    return ret


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))
lst = [[-1, -1, -1] for i in range(N+1)]
for i in range(N):
    lst[arr1[i]][0] = i+1
    lst[arr2[i]][1] = i+1
    lst[arr3[i]][2] = i+1
lst.sort()

res = 0

for a, b, c in lst[1:]:
    if getSum(startIndex+1, startIndex+b) > c:
        res += 1
    edit(startIndex+b, c)

print(res)

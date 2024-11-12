import sys
from math import ceil, log
input = sys.stdin.readline

N = int(input().strip())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2 - 1
tree[startIndex+1:startIndex+1+N] = list(map(int, input().split()))

def setTree(i):
    while i != 0:
        tree[i//2] += tree[i]
        i -= 1
setTree(startIndex+N)
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


M = int(input().strip())
c1 = []
c2 = []
idx = 0
for _ in range(M):
    cmd, *arg = map(int, input().split())
    if cmd == 1:
        # i, v = arg
        # editTree(startIndex + i, arg[v] - tree[startIndex + arg[i]])
        c1.append(arg)
    else:
        k, i, j = arg
        c2.append((k, i, j, idx))
        idx += 1
res = [0]*(len(c2))
c2.sort(reverse=True)
i, j = 0, 0
while c2:
    tk, ti, tj, tid = c2.pop()
    while i < tk:
        u, v = c1[i]
        editTree(startIndex + u, v - tree[startIndex + u])
        i += 1
    res[tid] = getSum(startIndex+ti, startIndex+tj)

for i in res:
    print(i)
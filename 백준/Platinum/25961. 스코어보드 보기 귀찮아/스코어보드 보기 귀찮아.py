import sys
from math import ceil, log
input = sys.stdin.readline

N, S = map(int, input().split())
Q = int(input().strip())
SIZE = Q
H = ceil(log(SIZE, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2

cnt = 0

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

def makeSum(start, K):
    cnt = 0
    idx, size = start-startIndex, 1
    while cnt < K and idx >= 0:
        if start % 2 == 0:  # 왼쪽 자식
            if tree[start] + cnt <= K:
                cnt += tree[start]
                idx = idx - size
                size = 1
                start = startIndex + idx
            elif size == 1:
                return idx+1
        else:
            if tree[start//2] + cnt < K:
                start //= 2
                size *= 2
            else:
                cnt += tree[start]
                idx = idx - size
                size = 1
                start = startIndex + idx

    return idx + 2

editTree(startIndex, N)

score = [0]*(N+1)
recent = [SIZE+3]*(N+1)
tR = N
for i in range(Q):
    t = int(input().strip())
    if t != 1 and score[t] == score[1] and recent[t] < recent[1]:
        tR -= 1
    recent[t] = i
    editTree(startIndex + score[t], -1)
    editTree(startIndex + score[t]+1, 1)
    score[t] += 1

    if t == 1:
        tR = tree[startIndex+score[1]]

    if score[1] == 0:
        rank = N
    else:
        rank = getSum(startIndex + score[1] + 1, startIndex + SIZE) + tR
    if rank > S:
        d = makeSum(startIndex+SIZE, S) - score[1]
    else:
        d = 0
    print(rank, d)


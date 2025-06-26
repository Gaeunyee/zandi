import sys
from math import ceil, log
input = sys.stdin.readline

size = 10**9 + 9
n, M, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
left = list(map(int, input().split()))
right = list(map(int, input().split()))
lst = []
inv = [-1]*(n+1)
left.sort()
right.sort()
idx = 0
flag = 1
for i in range(M):
    if left[i] <= right[i]:
        idx = max(left[i], idx)
        for k in range(idx, right[i]+1):
            inv[k] = len(lst)
            lst.append(arr[k])
        idx = right[i] + 1
    else:
        flag = 0
        break



def init(i):
    while i != 0:
        maxtree[i // 2] = max(maxtree[i // 2], maxtree[i])
        i -= 1


def edit(i, b):
    maxtree[i] = b
    i //= 2
    while i != 0:
        maxtree[i] = max(maxtree[i * 2 + 1], maxtree[i * 2])
        i //= 2

N = len(lst)
if flag:
    H = ceil(log(N, 2))
    treeSize = pow(2, H + 1)
    maxtree = [-size] * (treeSize + 1)
    startIndex = treeSize // 2
    for i in range(N):
        maxtree[startIndex + i] = lst[i]
    init(treeSize - 1)


if not flag:
    for _ in range(Q):
        i, j = map(int, input().split())
        print(10**9)
else:
    for _ in range(Q):
        i, j = map(int, input().split())
        if inv[i] >= 0 and inv[j] >= 0:
            arr[i], arr[j] = arr[j], arr[i]
            inv[i], inv[j] = inv[j], inv[i]
        elif inv[i] == -1 and inv[j] == -1:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            if inv[i] == -1:  # j가 없는쪽
                i, j = j, i
            edit(startIndex+inv[i], arr[j])
            arr[i], arr[j] = arr[j], arr[i]
        print(maxtree[1])


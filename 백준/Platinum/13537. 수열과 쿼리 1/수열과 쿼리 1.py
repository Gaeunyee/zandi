import sys
from math import ceil, log
input = sys.stdin.readline

N = int(input().strip())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2 - 1
sorted_tree = [[] for _ in range(treeSize+1)]
lst = [0]+list(map(int, input().split()))

def init(l, r, i):
    if l == r:
        sorted_tree[i].append(lst[l])
        return
    sorted_tree[i] = sorted(lst[l:r+1])
    init(l, (l+r)//2, i*2)
    init((l+r)//2+1, r, i*2+1)



def getSum(st, ed, l, r, i, k):
    if st <= l and r <= ed:
        return binarySearch(sorted_tree[i], k)
    elif st > r or ed < l:
        return 0
    else:
        return getSum(st, ed, l, (l+r)//2, i*2, k) + getSum(st, ed, (l+r)//2+1, r, i*2+1, k)

def binarySearch(arr, k):
    l, r = 0, len(arr)-1
    if arr[l] > k:
        return r+1
    elif arr[r] <= k:
        return 0
    while l+1 < r:
        m = (l+r)//2
        if arr[m] <= k:
            l = m
        else:
            r = m
    return len(arr)-r


init(1, N, 1)
Q = int(input().strip())
for _ in range(Q):
    i, j, k = map(int, input().split())
    print(getSum(i, j, 1, N, 1, k))

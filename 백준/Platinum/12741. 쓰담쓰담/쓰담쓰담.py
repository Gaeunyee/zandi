import sys
from math import ceil, log
input = sys.stdin.readline

N, Q = map(int, input().split())
H = ceil(log(N, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2 - 1
sorted_tree = [0]*(treeSize+1)
lst = [0]+list(map(int, input().split()))

def init(l, r, i):
    if l == r:
        sorted_tree[i] = 1
        return 1
    init(l, (l+r)//2, i*2)
    init((l+r)//2+1, r, i*2+1)
    if sorted_tree[i*2] and sorted_tree[i*2+1] and lst[(l+r)//2] <= lst[(l+r)//2+1]:
        sorted_tree[i] = 1


def editTree(l, r, i, k): # lst 수정은 따로
    if l == r:
        return 1
    if (l+r)//2 >= k:
        editTree(l, (l + r) // 2, i * 2, k)
    else:
        editTree((l + r) // 2 + 1, r, i * 2 + 1, k)
    if sorted_tree[i*2] and sorted_tree[i*2+1] and lst[(l+r)//2] <= lst[(l+r)//2+1]:
        sorted_tree[i] = 1
    else:
        sorted_tree[i] = 0


def getSum(st, ed, l, r, i):
    if st <= l and r <= ed:
        if sorted_tree[i]:
            return True
        else:
            return False
    elif st > r or ed < l:
        return True
    else:
        if getSum(st, ed, l, (l+r)//2, i*2) and getSum(st, ed, (l+r)//2+1, r, i*2+1):
            if ed <= (l+r)//2 or st >= (l+r)//2+1:
                return True
            elif lst[(l+r)//2] <= lst[(l+r)//2+1]:
                return True
            else:
                return False



init(1, N, 1)
for _ in range(Q):
    q, l, r = map(int, input().split())
    if q == 1:
        res = getSum(l, r, 1, N, 1)
        print("CS204") if res else print("HSS090")
    else:
        lst[l], lst[r] = lst[r], lst[l]
        editTree(1, N, 1, l)
        editTree(1, N, 1, r)



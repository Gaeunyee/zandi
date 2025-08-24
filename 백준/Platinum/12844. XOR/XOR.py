import sys
from math import ceil, log
input = sys.stdin.readline

N = int(input())
H = ceil(log(N, 2))
tree = [0] + [0]*(pow(2, H+1) - 1)
lazy = [0] + [0]*(pow(2, H+1) - 1)
nums = list(map(int, input().split()))
M = int(input())

def segment(left, right, i):
    if left == right:
        tree[i] = nums[left]
        return tree[i]
    mid = (left + right)//2
    tree[i] = segment(left, mid, i*2) ^ segment(mid+1, right, (i*2)+1)
    return tree[i]


segment(0, N-1, 1)


def seg_sum(start, end, idx, left, right):
    update_lazy(idx, start, end)
    if left > end or right < start:
        return 0
    if start >= left and right >= end:
        return tree[idx]
    mid = (start + end) // 2
    return seg_sum(start, mid, idx*2, left, right) ^ seg_sum(mid+1, end, idx*2+1, left, right)

def update_lazy(idx, start, end):
    if lazy[idx] != 0:
        tree[idx] ^= lazy[idx] if (end-start+1)%2 else 0
        if start != end:
            lazy[idx*2] ^= lazy[idx]
            lazy[idx*2+1] ^= lazy[idx]
        lazy[idx] = 0

def seg_edit2(idx, start, end, left, right, d):
    update_lazy(idx, left, right)
    if left > end or right < start:
        return 0
    if start <= left and right <= end:
        tree[idx] ^= d if (right-left+1)%2 else 0
        if left != right:
            lazy[idx*2] ^= d
            lazy[idx*2+1] ^= d
        return 0

    mid = (left + right) // 2
    seg_edit2(idx*2, start, end, left, mid, d)
    seg_edit2(idx*2+1, start, end, mid+1, right, d)
    tree[idx] = tree[idx*2] ^ tree[idx*2+1]

def solve():
    for _ in range(M):
        a, *b = map(int, input().split())
        if a == 1:
            seg_edit2(1, b[0], b[1], 0, N-1, b[2])
        else:
            x, y = b
            print(seg_sum(0, N-1, 1, min(x, y), max(x, y)))

solve()
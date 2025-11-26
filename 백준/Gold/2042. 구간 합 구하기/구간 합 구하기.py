import sys
from math import ceil, log
input = sys.stdin.readline

N, M, K = map(int, input().split())
H = ceil(log(N, 2))
tree = [0] + [0]*(pow(2, H+1) - 1)
nums = [int(input()) for i in range(N)]

def segment(left, right, i):
    if left == right:
        tree[i] = nums[left]
        return tree[i]
    mid = (left + right)//2
    tree[i] = segment(left, mid, i*2) + segment(mid+1, right, (i*2)+1)
    return tree[i]


segment(0, N-1, 1)


def seg_sum(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    if start >= left and right >= end:
        return tree[idx]
    mid = (start + end) // 2
    return seg_sum(start, mid, idx*2, left, right) + seg_sum(mid+1, end, idx*2+1, left, right)


def seg_edit(idx, target, left, right, d):
    if left > target or right < target:
        return 0
    tree[idx] += d
    if left != right:
        mid = (left + right) // 2
        seg_edit(idx*2, target, left, mid, d)
        seg_edit(idx*2+1, target, mid+1, right, d)


for _ in range(M+K):
    c, a, b = map(int, input().split())
    if c == 1:
        seg_edit(1, a - 1, 0, N - 1, b - nums[a - 1])
        nums[a - 1] = b
    else:
        print(seg_sum(0, N-1, 1, min(a, b)-1, max(a, b)-1))

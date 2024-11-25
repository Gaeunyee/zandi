import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [-1]+list(map(int, input().split()))
lst.append(10**18+7)
lst.sort()

def binarySearch2(key):
    l, r = 0, len(lst)
    while l+1 < r:
        mid = (l+r)//2
        if lst[mid] > key:
            r = mid
        else:
            l = mid
    return r


def binarySearch1(key):
    l, r = 0, len(lst)
    while l+1 < r:
        mid = (l+r)//2
        if lst[mid] >= key:
            r = mid
        else:
            l = mid
    return r

for _ in range(M):
    cmd, *x = map(int, input().split())
    if cmd == 1:
        print(len(lst)-binarySearch1(x[0])-1)
    if cmd == 2:
        print(len(lst)-binarySearch2(x[0])-1)
    if cmd == 3:
        print(binarySearch2(x[1])-binarySearch1(x[0]))

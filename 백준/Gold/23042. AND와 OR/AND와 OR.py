import sys
input = sys.stdin.readline

size = 30
mod = 10**9 + 7
N = int(input())
lst = list(map(int, input().split()))

one = [0]*size
for i in lst:
    for j in range(size):
        if i & (1<<j):
            one[j] += 1

res = 1
for i in range(N):
    t = 0
    for j in range(size):
        if one[j]:
            one[j] -= 1
            t += 1 << j
    res = (res*t)%mod

print(res)

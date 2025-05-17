import sys
input = sys.stdin.readline


N = int(input().strip())
lst = list(map(int, input().split()))
lst.sort()

j = N-1
res = 10**9 * 2 + 5
a, b = -1, -1
for i in range(N):
    if i >= j:
        break
    while i+1 < j and lst[i] + lst[j] > 0:
        j -= 1
    if j < N-1:
        if res > abs(lst[i]+lst[j+1]):
            a, b = lst[i], lst[j+1]
            res = abs(lst[i]+lst[j+1])
    if res > abs(lst[i] + lst[j]):
        a, b = lst[i], lst[j]
        res = abs(lst[i] + lst[j])


print(min(a, b), max(a, b))

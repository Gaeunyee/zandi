import sys
input = sys.stdin.readline


N = int(input().strip())
lst = list(map(int, input().split()))
lst.sort()
K = int(input().strip())

j = N-1
res = 0
for i in range(N):
    while i+1 < j and lst[i] + lst[j] > K:
        j -= 1
    if lst[i] + lst[j] == K:
        res += 1

print(res)

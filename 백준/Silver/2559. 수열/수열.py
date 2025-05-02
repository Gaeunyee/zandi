import sys
input = sys.stdin.readline


N, M = map(int, input().split())

lst = [0] + list(map(int, input().split()))
for i in range(1, N+1):
    lst[i] += lst[i-1]

res = -(10**9)
for i in range(N-M+1):
    res = max(res, lst[i+M]-lst[i])

print(res)


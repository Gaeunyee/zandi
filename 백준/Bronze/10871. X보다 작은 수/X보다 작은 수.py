import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))
res = []
for i in A:
    if i < X:
        res.append(i)

print(*res)


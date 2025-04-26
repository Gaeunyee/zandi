import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lst = set()
for _ in range(N):
    lst.add(input().strip())
res = 0
for _ in range(M):
    if input().strip() in lst:
        res += 1

print(res)

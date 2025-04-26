import sys
input = sys.stdin.readline


N = int(input().strip())
lst = []
for i in range(N):
    u, v = map(int, input().split())
    lst.append((v, u))

lst.sort()
for v, u in lst:
    print(u, v)


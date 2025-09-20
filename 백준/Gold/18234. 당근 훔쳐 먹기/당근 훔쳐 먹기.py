import sys
input = sys.stdin.readline
INF = 10**9

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
lst.sort(key=lambda x:x[1], reverse=True)
res = 0
t = M-1
for a, d in lst:
    res += a+t*d
    t -= 1

print(res)

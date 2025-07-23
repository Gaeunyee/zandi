import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
for _ in range(N):
    u, v = map(int, input().split())
    if u > v:
        lst.append((v, u))

lst.append((10**10, 10**10))
lst.sort()
end = -10**10
res = 0
for u, v in lst:
    if end < u:
        end = v
        res += v-u
    else:
        res += max(0, v - end)
        end = max(end, v)

print(2*res+M)

import sys

input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
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

print(res)

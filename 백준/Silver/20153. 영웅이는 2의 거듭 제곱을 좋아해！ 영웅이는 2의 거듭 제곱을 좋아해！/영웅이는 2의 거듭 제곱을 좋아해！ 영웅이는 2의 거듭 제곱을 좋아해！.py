import sys
input = sys.stdin.readline

N = int(input().strip())
a = list(map(int, input().split()))
s = 0
for i in a:
    s ^= i

res = s
for i in a:
    res = max(res, s^i)

print(str(res)+str(res))











import sys
input = sys.stdin.readline
mod = 900528

P = input().strip()
d = dict()
for i in range(len(P)):
    d[P[i]] = i+1
l = input().strip()
s = 1
res = 0
for i in l[::-1]:
    res += d[i] * s
    res %= mod
    s *= len(P)
    s %= mod
print(res)

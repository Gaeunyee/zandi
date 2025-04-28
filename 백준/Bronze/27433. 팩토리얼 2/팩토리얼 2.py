import sys
from math import sqrt, ceil

input = sys.stdin.readline


N = int(input().strip())
r = 1
for i in range(1, N+1):
    r *= i

print(r)


import sys
input = sys.stdin.readline

N = int(input().strip())
res = 1
for i in range(1, N+1):
    res *= i

print(res)

import sys
input = sys.stdin.readline

INF = 10**9


N = int(input().strip())
arr = [0]*N
l = N//2

size = 1
t = -1
for i in range(N, 0, -1):
    arr[l] = i
    l += size*t
    size += 1
    t *= -1

print(*arr)


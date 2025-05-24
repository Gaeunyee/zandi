import sys
input = sys.stdin.readline

INF = 10**9


N = int(input().strip())
arr = [0]*N
d = [0, N//2, -(N//2+1)]
t = 1
l = N//2 + N % 2
for i in range(N):
    arr[i] = l
    l += d[t]
    t *= -1

print(*arr)


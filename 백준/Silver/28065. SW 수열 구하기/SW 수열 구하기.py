import sys
input = sys.stdin.readline

INF = 10**9


N = int(input().strip())
arr = [0]*N
l = N
size = N
t = -1
for i in range(N):
    arr[i] = l
    size -= 1
    l += (size)*t
    t *= -1

print(*arr)


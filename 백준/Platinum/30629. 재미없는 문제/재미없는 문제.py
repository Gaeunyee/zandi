import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0]*(N+1)
rest = M
k = N//2+1
length = N-1

if rest > length:
    for i in range(2, k+1):
        arr[i] += 1
    rest -= k-1
    for i in range(k+1, N+1):
        if rest < k:
            arr[i] += rest
            break
        arr[i] += k
        rest -= k
else:
    for i in range(N, N-rest, -1):
        arr[i] += 1



print(*arr[1:])


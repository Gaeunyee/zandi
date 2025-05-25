import sys
input = sys.stdin.readline

INF = 10**9


N, K = map(int, input().split())

if N == K:
    print("Impossible")
else:
    t = N-K
    arr = [0]*(N+1)
    for i in range(1, t):
        arr[i] = i+1
    arr[t] = 1
    for i in range(t+1, N+1):
        arr[i] = i

    print(*arr[1:])



import sys
INF = 1 << 64 - 1
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
res = [A[i]*B[i] for i in range(N)]

print(sum(res))


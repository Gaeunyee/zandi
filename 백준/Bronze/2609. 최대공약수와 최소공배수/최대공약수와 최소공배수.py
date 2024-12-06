import sys
input = sys.stdin.readline


#sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
gcd = 0
for i in range(1, min(N, K)+1):
    if N % i == K % i == 0:
        gcd = i

print(gcd)
print(N*K//gcd)
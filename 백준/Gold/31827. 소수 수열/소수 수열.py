import sys
input = sys.stdin.readline
INF = 10**6
N, K = map(int, input().split())
Primes = [True]*(INF+7)
mod = [[] for _ in range(K)]
for i in range(2, INF+1):
    if Primes[i]:
        mod[i % K].append(i)
    k = 2
    while i*k < INF+3:
        Primes[i*k] = False
        k += 1

print(*mod[-1][:N])


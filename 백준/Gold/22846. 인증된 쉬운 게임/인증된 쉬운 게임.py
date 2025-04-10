import sys
input = sys.stdin.readline
INF = 10**5

K = int(input().strip())

def sieve_of_eratosthenes(n):
    primes = [[] for _ in range(n+1)]
    primes[1].append(1)
    for i in range(1, int(n**0.5) + 1):
        for j in range(i*2, n+1, i):
            primes[j].append(i)
    return primes


graph = sieve_of_eratosthenes(K+1)
dp = [0]*(K+1)
for i in range(K-1, 0, -1):
    for p in graph[i]:
        a, b = i+p, i+(i//p)
        if a <= K and not dp[a]:
            dp[i] = 1
        if b <= K and not dp[b]:
            dp[i] = 1


print("Kali" if dp[1] else "Ringo")


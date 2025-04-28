import sys
from math import sqrt, ceil
input = sys.stdin.readline
size = 10**6
isPrime = [1]*size
primes = []
for i in range(2, int(sqrt(size))+1):
    if isPrime[i]:
        t = i*2
        while t < size:
            isPrime[t] = 0
            t += i

for i in range(2, size):
    if isPrime[i]:
        primes.append(i)


N, M = map(int, input().split())
for i in primes:
    if N <= i <= M:
        print(i)
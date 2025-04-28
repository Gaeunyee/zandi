import sys
from math import sqrt, ceil
input = sys.stdin.readline
size = 10**5
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


T = int(input().strip())
s = 10**4 * 2
for _ in range(T):
    N = int(input().strip())
    if N == 1 or N == 0:
        print(2)
        continue
    lst = [1]*s
    hi = min(N-1, int(sqrt(N))+1)
    for i in primes:
        if i > hi:
            break
        j = ceil(N/i)*i
        while j < N+s:
            lst[j-N] = 0
            j += i

    for i in range(s):
        if lst[i]:
            print(i+N)
            break



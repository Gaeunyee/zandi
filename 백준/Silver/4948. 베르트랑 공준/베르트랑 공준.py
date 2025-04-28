import sys
from math import sqrt, ceil
from bisect import *

input = sys.stdin.readline
size = 10**5 * 3
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


while True:
    t = int(input().strip())
    if t == 0:
        break
    r, l = bisect_right(primes, 2*t, 0, len(primes)), bisect_left(primes, t, 0, len(primes))
    print(r - (l if primes[l] != t else l+1))



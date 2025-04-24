import sys
import math
input = sys.stdin.readline

M = int(input().strip())
N = int(input().strip())
def isPrime(i):
    if i == 1:
        return False
    for j in range(2, min(i-1, int(math.sqrt(i))+3)):
        if i % j == 0:
            return False
    return True


r = 0
s = 0
for i in range(M, N+1):
    if isPrime(i):
        if r == 0:
            r = i
        s += i
if s:
    print(s)
    print(r)
else:
    print(-1)


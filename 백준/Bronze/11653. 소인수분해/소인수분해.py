import sys
import math
input = sys.stdin.readline

N = int(input().strip())
def isPrime(i):
    ret = []
    if i == 1:
        return ret
    for j in range(2, min(i+1, int(math.sqrt(i))+3)):
        if i % j == 0:
            while i % j == 0:
                ret.append(j)
                i //= j
    if i != 1:
        ret.append(i)
    return ret


for i in isPrime(N):
    print(i)

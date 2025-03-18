import sys
input = sys.stdin.readline

#sys.setrecursionlimit(10**5)
INF = 10 ** 6

N = int(input().strip())
a, b = 1, 2
for i in range(N-1):
    a, b = b, a+b

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

c = gcd(a, b)
print(a//c)




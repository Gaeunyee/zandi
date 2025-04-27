import sys
input = sys.stdin.readline
m = 10**9 + 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    while True:
        if b == 0:
            return a
        a, b = b, a % b


a, b = map(int, input().split())
c, d = map(int, input().split())
A, B = a*d + b*c, b*d
g = gcd(A, B)
print(A//g, B//g)



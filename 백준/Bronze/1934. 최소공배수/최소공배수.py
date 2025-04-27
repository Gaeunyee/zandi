import sys
input = sys.stdin.readline
m = 10**9 + 7

T = int(input().strip())
def gcd(a, b):
    while True:
        if b == 0:
            return a
        a, b = b, a % b


for _ in range(T):
    A, B = map(int, input().split())
    if A < B:
        A, B = B, A
    print(A*B//gcd(A, B))



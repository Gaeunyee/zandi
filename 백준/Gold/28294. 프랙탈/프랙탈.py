import sys
input = sys.stdin.readline
m = 10**9 + 7
def pow(a, p, m):
    bin_B = str(bin(p))
    n = a % m
    res = 1
    for i in reversed(bin_B):
        if i == '1':
            res *= n
        n = (n % m) ** 2
        n %= m
    return res
N, a = map(int, input().split())
print(((N*(N-2)) % m * (pow(N, a, m) - pow(N-1, a, m)) % m + pow(N, a+1, m)) % m)


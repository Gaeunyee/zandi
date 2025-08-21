import sys
input = sys.stdin.readline



def pow(n, p, mod):
    ret = 1
    d = n
    while p:
        if p % 2 == 1:
            ret *= d
            ret %= mod
        d = (d % mod) ** 2
        d %= mod
        p //= 2
    return ret

def isPrime(n):
    prime = [2, 7, 61]
    d = n - 1
    h = 0
    while d % 2 == 0:
        d //= 2
        h += 1

    for a in prime:
        flag = 0
        if a >= n:
            flag = 1
            continue
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            flag = 1
            continue

        k = pow(a, 2, n)
        for j in range(0, h):
            if pow(k, d, n) == n-1:
                flag = 1
                break
            k = pow(k, 2, n)
        if not flag: # 합성수임
            return 0
    return 1

while True:
    p, a = map(int, input().split())
    if p == a == 0:
        break
    if not isPrime(p) and pow(a, p, p) == a:
        print('yes')
    else:
        print('no')

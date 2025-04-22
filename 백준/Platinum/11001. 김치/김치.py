import sys
input = sys.stdin.readline

INF = (1 << 64)-1
N, D = map(int, input().split())
tmp = [0]+list(map(int, input().split()))
val = [0]+list(map(int, input().split()))

dp = [0]*(N+1)
mem = [0]*(N+1)
def DnC(s, e, l, r):
    res = 0
    d = (l+r)//2
    K = -1
    for k in range(max(s, d-D), min(d+1, e+1)):
        t = val[k]+tmp[d]*(d-k)
        if t >= res:
            res = t
            K = k
    dp[d] = res
    mem[d] = K
    if l != d:
        DnC(s, K, l, d - 1)
    if r != d:
        DnC(K, e, d + 1, r)


DnC(1, N, 1, N)

print(max(dp))
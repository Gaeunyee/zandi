import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)
INF = (1 << 64)-1
L, G = map(int, input().split())
arr = [0]+list(map(int, input().split()))
dp = [[0]*(L+1) for _ in range(G+1)]
S = [0]*(L+1)
for i in range(1, L+1):
    S[i] += S[i-1]+arr[i]
    dp[1][i] = S[i]*i

def DnC(s, e, l, r, i):
    res = INF
    d = (l+r)//2
    K = -1
    for k in range(s, min(d+1, e+1)):
        t = dp[i-1][k]+(S[d]-S[k])*(d-k)
        if t <= res:
            res = t
            K = k
    dp[i][d] = res

    if l != d:
        DnC(s, K, l, d-1, i)
    if r != d:
        DnC(K, e, d+1, r, i)

for i in range(2, G+1):
    DnC(1, L, 1, L, i)

print(dp[min(G, L)][L])


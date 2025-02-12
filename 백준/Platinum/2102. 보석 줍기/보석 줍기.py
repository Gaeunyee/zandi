import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jw = [0]
S = [0]*(N+1)

for _ in range(N):
    jw.append(int(input().strip()))

for i in range(1, N+1):
    S[i] += S[i-1] + jw[i]

def search(x):
    i = 1
    mi = 0
    for j in range(M, N+1):
        while i+M-1 <= j and mi > 1000*S[j]-x*j:
            mi = min(mi, 1000 * S[i - 1] - x * (i - 1))
            i += 1
        if mi <= 1000*S[j]-x*j:
            return True
    return False

l, r = -1, 2000001
while l+1 < r:
    m = (l+r)//2
    if search(m):
        l = m
    else:
        r = m

print(l)

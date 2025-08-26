import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
m, M = 3000000, 0
res = 0
for i in lst:
    m = min(m, i)
    M = max(M, i)
    if M-m >= K:
        res += 1
        m, M = i, i
print(res)

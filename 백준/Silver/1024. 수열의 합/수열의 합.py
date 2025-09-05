import sys
input = sys.stdin.readline

N, L = map(int, input().split())
res = -1
for i in range(L, 101):
    t = (2*N-i*i+i)%(2*i)
    if (2*N-i*i+i)%(2*i) or (2*N-i*i+i)//(2*i) < 0:
        continue
    res = i
    break

if res != -1:
    print(*range((2*N-res*res+res)//(2*res), (2*N-res*res+res)//(2*res)+res))
else:
    print(res)
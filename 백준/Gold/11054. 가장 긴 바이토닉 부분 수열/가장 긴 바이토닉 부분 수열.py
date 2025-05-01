import sys
input = sys.stdin.readline

N = int(input().strip())
lst = list(map(int, input().split()))
dp_f = [1]*N
dp_b = [1]*N
for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            dp_f[i] = max(dp_f[i], dp_f[j]+1)

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if lst[j] < lst[i]:
            dp_b[i] = max(dp_b[i], dp_b[j]+1)
res = 0
for i in range(N):
    res = max(res, dp_f[i] + dp_b[i] - 1)

print(res)

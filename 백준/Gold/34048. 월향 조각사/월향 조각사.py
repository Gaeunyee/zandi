import sys
input = sys.stdin.readline
mod = 987654321

N = int(input())
lst = list(map(int, input().split())) + [0]
dp_l = [0]*(N+1)
dp_r = [0]*(N+1)
for i in range(N):
    if dp_l[i-1] < lst[i]:
        dp_l[i] = dp_l[i-1]+1
    else:
        dp_l[i] = lst[i]

for i in range(N-1, -1, -1):
    if dp_r[i+1] < lst[i]:
        dp_r[i] = dp_r[i+1]+1
    else:
        dp_r[i] = lst[i]
res = 0
for i in range(N):
    res += min(dp_l[i], dp_r[i])

print(res)

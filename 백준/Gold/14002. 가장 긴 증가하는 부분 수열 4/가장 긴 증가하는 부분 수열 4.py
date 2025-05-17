import sys
input = sys.stdin.readline


N = int(input().strip())
lst = list(map(int, input().split()))
dp = [1]*N
par = [-1]*N
for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            if dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
                par[i] = j
m = max(dp)
tr = dp.index(m)
print(m)
res = []
while True:
    res.append(lst[tr])
    if dp[tr] == 1:
        break
    tr = par[tr]
print(*res[::-1])


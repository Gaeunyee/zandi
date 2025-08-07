import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [0]*5
dp[0] = 1
s = [lst[0]]
for i in range(1, N):
    s.append(lst[i]+s[-1])

d = s[-1]
if d != 0:
    t = d//4
    s.append(0)

    for i in range(N):
        if s[i]%t == 0:
            dp[s[i]//t] += dp[s[i]//t-1]

    print(dp[4])
else:
    cnt = 0
    for i in range(N-1):
        if s[i] == 0:
            cnt += 1

    print(cnt*(cnt-1)*(cnt-2)//6)

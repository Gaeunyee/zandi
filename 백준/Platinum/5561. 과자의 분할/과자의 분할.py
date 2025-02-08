import sys
input = sys.stdin.readline

N = int(input().strip())
INF = 10**9+7
size = N+1
P = []
for _ in range(N-1):
    P.append(int(input().strip()))

dp1 = [INF]*size
dp2 = [INF] + [0] + [INF]*(size-2)

for i in range(1, N):
    if i % 2 == 1:
        dp1[1] = P[i - 1]
    else:
        dp2[1] = P[i - 1]
    for j in range(2, size):
        if i % 2 == 1:
            dp1[j] = dp2[j-1]
            if i >= j:
                dp1[j] = min(dp1[j], dp2[i-j+1] + P[i-1])

        else:
            dp2[j] = dp1[j-1]
            if i >= j:
                dp2[j] = min(dp2[j], dp1[i-j+1] + P[i-1])


print(dp1[N//2])

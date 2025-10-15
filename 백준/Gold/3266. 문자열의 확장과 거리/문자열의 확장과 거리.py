import sys
input = sys.stdin.readline
size = 101
m = -100000000

A = input().strip()
B = input().strip()
N = int(input())


dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
for i in range(len(A)):
    dp[i][len(B)] = N*(i+1)
for i in range(len(B)):
    dp[len(A)][i] = N*(i+1)

for i in range(len(A)):
    for j in range(len(B)):
        dp[i][j] = min(dp[i-1][j-1]+abs(ord(A[i])-ord(B[j])), dp[i][j-1]+N, dp[i-1][j]+N)

print(dp[len(A)-1][len(B)-1])

import sys
input = sys.stdin.readline

A = '$'+input().strip()
B = '$'+input().strip()

dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]


for i in range(1, len(A)):
    for j in range(1, len(B)):
        dp[i][j] = (dp[i-1][j-1] + 1) if A[i] == B[j] \
            else max(dp[i-1][j], dp[i][j-1])


print(dp[len(A)-1][len(B)-1])
if dp[len(A)-1][len(B)-1]:
    i, j = len(A)-1, len(B)-1
    res = ''
    while dp[i][j] != 0:
        if A[i] == B[j]:
            res += A[i]
            i, j = i - 1, j - 1
        else:
            if dp[i][j - 1] > dp[i - 1][j]:
                i, j = i, j - 1
            else:
                i, j = i - 1, j
    print(res[::-1])

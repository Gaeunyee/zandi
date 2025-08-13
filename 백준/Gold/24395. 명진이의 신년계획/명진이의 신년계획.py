import sys
input = sys.stdin.readline
size = 51

N, M = map(int, input().split())
lst = []
for _ in range(M):
    lst.append(tuple(map(int, input().split())))

dp = [[-1]*size for _ in range(size)]
dp[0][0] = 0
for r, b, d in lst:
    for i in range(size-1, r-1, -1):
        for j in range(size-1, b-1, -1):
            if dp[i-r][j-b] != -1:
                dp[i][j] = max(dp[i-r][j-b]+d, dp[i][j])

st = []
for i in range(1, N+1):
    r, b = map(int, input().split())
    if dp[r][b] != -1:
        st.append((dp[r][b], i))
    else:
        st.append((0, i))

st.sort()
for d, i in st:
    print(i, d)

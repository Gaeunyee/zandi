import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
S = [-1]+list(map(int, input().split()))
joint = [0]*(N+1)

for _ in range(M):
    i, j = map(int, input().split())
    if (i, j) == (1, N) or (i, j) == (N, 1):
        joint[N] = 1
    else:
        joint[min(i, j)] = 1

st = []
res = 0
start = 0
for i in range(1, N):
    st.append(S[i])
    if joint[i]:
        a = min(st)
        if res == 0:
            start = a
        res += a
        st = []
st.append(S[N])
a = min(st)
if not joint[N] and start:
    res -= start
    res += min(start, a)
else:
    res += a

if M <= 1:
    print('YES')
elif res <= K:
    print('YES')
else:
    print('NO')



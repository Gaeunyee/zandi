import sys
input = sys.stdin.readline


N = int(input().strip())

c1 = [0]*(2*N)
col = [0]*(2*N)
c2 = [0]*(2*N)
cnt = 0

def backTrack(idx):
    global cnt
    if idx == N:
        cnt += 1
        return

    for n in range(N):
        if not c1[n+idx] and not c2[n-idx] and not col[n]:
            c1[n+idx], c2[n-idx], col[n] = 1, 1, 1
            backTrack(idx+1)
            c1[n+idx], c2[n-idx], col[n] = 0, 0, 0


backTrack(0)
print(cnt)

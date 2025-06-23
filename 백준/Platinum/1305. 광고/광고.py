import sys
input = sys.stdin.readline

N = int(input().strip())
txt = input().strip()
F = [0]*N


def FailureFunction(pattern, N):
    i, j = 1, 0
    while i < N:
        if pattern[i] == pattern[j]:
            F[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = F[j-1]
        else:
            F[i] = 0
            i += 1


FailureFunction(txt, N)
res = N - F[N-1]
for i in range(1, N):
    if F[i]*2 == i+1:
        f = 0
        for d in range(1, N):
            if i + d*F[i] >= N:
                break
            if F[i + d*F[i]] == (d+1)*F[i]:
                f = d
                continue
            else:
                f = 0
                break
        if f:
            idx = 0
            for j in range(i + f*F[i]+1, N):
                if txt[idx] == txt[j]:
                    idx += 1
                else:
                    f = 0
                    break
        if f:
            res = F[i]
            break
print(res)

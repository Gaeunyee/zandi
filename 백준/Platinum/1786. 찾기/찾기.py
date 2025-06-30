import sys

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


def KMP(txt, pattern, N):
    i, j = 0, 0
    idx = []
    while i < len(txt):
        if txt[i] == pattern[j]:
            i += 1
            j += 1
            if j == N:
                idx.append(i-N+1)
                j = F[j-1]
        elif j > 0:
            j = F[j-1]
        else:
            i += 1
            j = 0
    return idx


T = input()
P = input()
F = [0]*len(P)
FailureFunction(P, len(P))

def setFraction(a, b):
    while b != 0:
        a, b = b, a % b

    return a

ok = KMP(T, P, len(P))
print(len(ok))
print(*ok)

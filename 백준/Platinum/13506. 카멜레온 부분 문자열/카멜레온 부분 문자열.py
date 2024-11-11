import sys
input = sys.stdin.readline

line1 = input().strip()
N = len(line1)
F = [0]*N
table = []
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
    idx = 0
    while i < N-2:
        if txt[i] == pattern[j]:
            if j == table[idx]-1:
                if idx == len(table)-1:
                    return idx
                idx += 1
            i += 1
            j += 1

        elif j > 0:
            j = F[j-1]
        else:
            i += 1
            j = 0
    if idx == 0:
        return -1
    return idx - 1



FailureFunction(line1, N)
i = F[-1]
while i > 0:
    table.append(i)
    i = F[i-1]
table.sort()
l = -1
if table:
    l = KMP(line1[1:-1], line1, N)
if l != -1:
    print(line1[:table[l]])
else:
    print(-1)


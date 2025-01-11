import sys
input = sys.stdin.readline

N = int(input().strip())

def FailureFunction(pattern, size):
    i, j = 1, 0
    while i < size:
        if pattern[i]-pattern[i-j] == pattern[j]-pattern[0]:
            F[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = F[j-1]
        else:
            F[i] = 0
            i += 1


def KMP(txt, pattern, size, SIZE):
    i, j = 0, 0
    while i < SIZE:
        if txt[i]-txt[i-j] == pattern[j]-pattern[0]:
            if j == size-1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = F[j-1]
        else:
            i += 1
            j = 0
    return False

lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))

L = int(input().strip())
melody = tuple(map(int, input().split()))
F = [0]*L
FailureFunction(melody, L)
flag = 0
res = []
for i in range(N):
    if KMP(lst[i][1:], melody, L, lst[i][0]):
        res.append(i+1)

if res:
    print(*res)
else:
    print(-1)



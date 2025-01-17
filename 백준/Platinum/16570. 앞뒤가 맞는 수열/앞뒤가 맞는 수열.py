import sys
input = sys.stdin.readline


N = int(input().strip())
F = [0]*N
lst = list(map(int, input().split()))


def FailureFunction(pattern, N):
    i, j = 1, 0
    maximum, cnt = 0, 0
    while i < N:
        if pattern[i] == pattern[j]:
            F[i] = j + 1
            i += 1
            j += 1
            if j > maximum:
                maximum = j
                cnt = 1
            elif j == maximum:
                cnt += 1
        elif j > 0:
            j = F[j-1]
        else:
            F[i] = 0
            i += 1
    return maximum, cnt

lst.reverse()
a, b = FailureFunction(lst, N)
if a == 0:
    print(-1)
else:
    print(a, b)


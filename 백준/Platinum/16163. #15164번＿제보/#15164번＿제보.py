import sys
from collections import deque

input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

S = '#'.join(input().strip())


def Manacher(S):
    size = len(S)
    A = [0]*size
    r, c = -1, -1
    for i in range(size):
        if i <= r:
            A[i] = min(r - i, A[2*c-i])

        while i+A[i]+1<size and i-A[i]-1>=0 and S[i-A[i]-1] == S[i+A[i]+1]:
            A[i] += 1

        if r < i+A[i]:
            r = i + A[i]
            c = i
    res = 0
    for i in range(size):
        res += A[i]//2
        if S[i] != '#' or S[i+A[i]] != '#':
            res += 1

    return res

print(Manacher(S))

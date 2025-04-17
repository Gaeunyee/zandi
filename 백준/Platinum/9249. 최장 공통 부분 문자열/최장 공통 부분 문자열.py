import sys
from functools import cmp_to_key
input = sys.stdin.readline


def make_compare(t, group):
    def compare(a, b):
        if group[a] != group[b]:
            if group[a] < group[b]:
                return -1
            else:
                return 1
        if group[a + t] < group[b + t]:
            return -1
        else:
            return 1
    return compare

def solve():
    A, B = input().strip(), input().strip()
    string = A+"$"+B
    la, lb = len(A), len(string)

    N = len(string)
    group = [ord(string[i]) for i in range(N)]
    t = 1
    group.append(-1)
    res = [i for i in range(N)]
    while t < N:
        cmp = make_compare(t, group)
        res.sort(key=cmp_to_key(cmp))
        t *= 2
        newGroup = [0]*(N+1)
        newGroup[N], newGroup[res[0]] = -1, 0
        for i in range(1, N):
            if cmp(res[i-1], res[i]) == -1:
                newGroup[res[i]] = newGroup[res[i-1]] + 1
            else:
                newGroup[res[i]] = newGroup[res[i-1]]
        group = newGroup

        if t >= N:
            break

    ir = [0]*N
    for i in range(N):
        ir[res[i]] = i
    lcp = [0]*N
    d = 0
    string += '@'
    if N == 1:
        print(0)
        exit()
    for i in range(N):
        if ir[i] == 0:
            continue
        while string[i+d] == string[res[ir[i]-1]+d]:
            d += 1
        lcp[ir[i]] = d
        d = max(0, d-1)

    m = 0
    idx = -1
    for i in range(1, N):
        if 0 <= res[i] < la and la < res[i-1] < N and lcp[i] > m:
            m = lcp[i]
            idx = res[i]
        if 0 <= res[i-1] < la and la < res[i] < N and lcp[i] > m:
            m = lcp[i]
            idx = res[i]

    print(m)
    print(string[idx:idx+m])



solve()

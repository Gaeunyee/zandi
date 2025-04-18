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
    string = input().strip()
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
    for i in range(N):
        print(res[i])

solve()

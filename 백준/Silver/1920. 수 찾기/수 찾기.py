import sys
input = sys.stdin.readline


def solve():
    N = int(input().strip())
    lst = list(map(int, input().split()))
    lst.sort()

    M = int(input().strip())
    query = []
    i = 0
    for n in map(int, input().split()):
        query.append((n, i))
        i += 1

    query.sort()
    res = [0]*M
    idx = 0
    for n, i in query:
        while n > lst[idx] and idx < N-1:
            idx += 1
        if lst[idx] == n:
            res[i] = 1
        else:
            res[i] = 0
    for i in res:
        print(i)

solve()

import sys
from collections import deque
size = 10000
input = sys.stdin.readline

T = int(input().strip())


def lshift(n):
    sn = str(n).rjust(4, '0')
    return int(sn[1:] + sn[0])


def rshift(n):
    sn = str(n).rjust(4, '0')
    return int(sn[-1] + sn[:-1])


def solve():
    A, B = map(int, input().split())
    par = [-1] * size
    cmd = [0]*size
    qu = deque()
    qu.append(A)
    while qu:
        t = qu.popleft()
        nxt = [(t*2)%size, (t-1)%size, lshift(t), rshift(t)]
        for i in range(4):
            n = nxt[i]
            if par[n] == -1:
                par[n] = t
                cmd[n] = i
                qu.append(n)

    res = []
    tr = B
    c = "DSLR"
    while tr != A:
        res.append(cmd[tr])
        tr = par[tr]

    for i in range(len(res)-1, -1, -1):
        print(c[res[i]], end='')
    print()

for _ in range(T):
    solve()


import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, Q, K = map(int, input().split())
    st = []
    cmd = [-1]
    t = 1
    start = 0
    for i in range(Q):
        c, *p = map(int, input().split())
        if c == 1:
            start = i+1
            cmd.append(-1)
        elif c == 2:
            cmd.append(-2)
        else:
            cmd.append(p[0])

    for i in range(start):
        if cmd[i] > 0:
            st.append(cmd[i])
    st.sort()
    qu = deque(st)
    for i in range(start+1, Q+1):
        if cmd[i] == -2:
            t *= -1
        elif t == 1:
            qu.appendleft(cmd[i])
        else:
            qu.append(cmd[i])

    if t == 1:
        print(qu[K-1])
    else:
        print(qu[-K])


solve()

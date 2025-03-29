import sys
from functools import cmp_to_key
input = sys.stdin.readline


def ccw(a, b, c):
    x1, x2 = b[0]-a[0], c[0]-a[0]
    y1, y2 = b[1]-a[1], c[1]-a[1]
    return x1*y2 - x2*y1


def compare(a, b):
    c = ccw(u, a, b)
    if c > 0:
        return -1
    elif c < 0:
        return 1
    else:
        if (u[0]-a[0])**2 + (u[1]-a[1])**2 > (u[0]-b[0])**2 + (u[1]-b[1])**2:
            return 1
        else:
            return -1


def makeConvexHull(dot):
    dot.sort(key=cmp_to_key(compare))
    st = [dot[0], dot[1]]
    for nxt in dot[2:]:
        while len(st) >= 2 and ccw(st[-2], st[-1], nxt) <= 0:
            st.pop()
        st.append(nxt)
    return st


N = int(input().strip())
dot = []
for _ in range(N):
    dot.append(tuple(map(int, input().split())))
dot.sort()
u = dot[0]
print(len(makeConvexHull(dot)))

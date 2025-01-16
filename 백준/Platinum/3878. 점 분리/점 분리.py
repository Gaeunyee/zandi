import sys
from functools import cmp_to_key
input = sys.stdin.readline

def ccw(a, b, c):
    tmp = (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (b[0]*a[1] + c[0]*b[1] + a[0]*c[1])
    if tmp > 0:
        return 1
    if tmp < 0:
        return -1
    if tmp == 0:
        return 0

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


def overLab(a, b, c, d):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    x4, y4 = d
    if ((min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2)) and
            (min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2))):
        return True
    return False


def isCross(a, b, c, d):
    u = ccw(a, b, c) * ccw(a, b, d)
    v = ccw(c, d, a) * ccw(c, d, b)
    if u == 0 and v == 0:
        return overLab(a, b, c, d)
    elif u <= 0 and v <= 0:
        return True
    else:
        return False


def isIn(point, shape):
    x, y = point
    for i in range(len(shape)-1):
        ex, ey = x - shape[i + 1][0], y - shape[i + 1][1]
        dx, dy = shape[i][0] - shape[i + 1][0], shape[i][1] - shape[i + 1][1]
        dot = ex * dy - ey * dx
        if dot < 0:
            return False
    return True

def solve(b, w):
    if len(b) == 1 and len(w) == 1:
        return True
    if len(b) >= 4:
        for i in w:
            if isIn(i, b):
                return False
    elif len(b) == 2:
        if len(w) == 1:
            if ccw(b[0], b[1], w[0]) == 0 and min(b[0][0], b[1][0]) <= w[0][0] <= max(b[0][0], b[1][0]):
                return False
            else:
                return True
        for i in range(len(w)-1):
            if isCross(b[0], b[1], w[i], w[i+1]):
                return False
    if len(w) >= 4:
        for i in b:
            if isIn(i, w):
                return False
    elif len(w) == 2:
        if len(b) == 1:
            if ccw(w[0], w[1], b[0]) == 0 and min(w[0][0], w[1][0]) <= b[0][0] <= max(w[0][0], w[1][0]):
                return False
            else:
                return True
        for i in range(len(b)-1):
            if isCross(w[0], w[1], b[i], b[i+1]):
                return False
    return True


T = int(input().strip())
for _ in range(T):
    n, m = map(int, input().split())

    black_points = []
    for _ in range(n):
        black_points.append(tuple(map(int, input().split())))
    if n >= 3:
        black_points.sort()
        u = black_points[0]
        black_points = makeConvexHull(black_points)
        black_points.append(u)

    white_points = []
    for _ in range(m):
        white_points.append(tuple(map(int, input().split())))
    if m >= 3:
        white_points.sort()
        u = white_points[0]
        white_points = makeConvexHull(white_points)
        white_points.append(u)

    if solve(black_points, white_points):
        print('YES')
    else:
        print('NO')

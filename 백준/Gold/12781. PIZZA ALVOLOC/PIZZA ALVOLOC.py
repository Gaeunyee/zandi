import sys
input = sys.stdin.readline

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())


def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if tmp > 0:
        return 1
    if tmp < 0:
        return -1
    if tmp == 0:
        return 0


def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    a = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    b = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    if a < 0 and b < 0:
        return True
    else:
        return False


if isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    print(1)
else:
    print(0)

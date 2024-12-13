import sys
from math import sqrt
input = sys.stdin.readline


def area(a, b, c):
    s = a+b+c
    s /= 2
    k = s*(s-a)*(s-b)*(s-c)
    if k >= 0:
        return sqrt(s*(s-a)*(s-b)*(s-c))
    else:
        return -1

def isTriangle(a, b, c):
    l = sorted([a, b, c])
    if l[2] < l[0]+l[1]:
        return 1
    elif l[2] == l[0]+l[1]:
        return 0
    return -1


matrix = []
for i in range(4):
    matrix.append(list(map(int, input().split())))


def solve():
    mask = [(0, 1, 2, 3), (0, 1, 3, 2)]
    flag = 1

    i, j, k, e = (0, 1, 2, 3)
    a, b, c = matrix[i][j], matrix[j][k], matrix[k][i]
    t = isTriangle(a, b, c)
    if t == -1:
        return False
    x1 = (a ** 2 + b ** 2 - c ** 2) / (a << 1)
    y1 = sqrt(b ** 2 - x1 ** 2)

    i, j, k, e = (0, 1, 3, 2)
    a, b, c = matrix[i][j], matrix[j][k], matrix[k][i]
    t = isTriangle(a, b, c)
    if t == -1:
        return False
    x2 = (a ** 2 + b ** 2 - c ** 2) / (a << 1)
    y2 = sqrt(b ** 2 - x2 ** 2)
    if sqrt((x2-x1)**2 + (y2-y1)**2) <= matrix[2][3] <= sqrt((x2-x1)**2 + (y2+y1)**2):
        return True
    return False



if solve():
    print("YES")
else:
    print("NO")

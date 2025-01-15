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


T = int(input().strip())
for _ in range(T):
    l = list(map(int, input().split()))
    dot = []
    for i in range(l[0]):
        dot.append((l[i*2+1], l[i*2+2], i))
    dot.sort()
    u = dot[0]
    dot.sort(key=cmp_to_key(compare))
    k = -1
    while ccw(u, dot[k], dot[k-1]) == 0:
        k -= 1
    for i in dot[:k]:
        print(i[2], end=' ')
    for i in reversed(dot[k:]):
        print(i[2], end=' ')
    print()





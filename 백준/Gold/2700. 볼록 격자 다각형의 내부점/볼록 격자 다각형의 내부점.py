import sys
input = sys.stdin.readline

P = int(input().strip())


def isIn(x, y):
    for i in range(N):
        ex, ey = x - shape[i + 1][0], y - shape[i + 1][1]
        dx, dy = shape[i][0]-shape[i+1][0], shape[i][1]-shape[i+1][1]
        dot = ex*dy - ey*dx
        if dot >= 0:
            return False
    return True


def solve():
    for i in range(-30, 31):
        for j in range(-30, 31):
            if isIn(i, j):
                height[j][0] = min(i, height[j][0])
                height[j][1] = max(i, height[j][1])


for _ in range(P):
    N = int(input().strip())
    shape = []
    for _ in range(N):
        shape.append(tuple(map(int, input().split())))
    shape.append(shape[0])
    height = [[31, -31] for _ in range(61)]
    solve()
    res = []
    for i in range(-30, 31):
        if height[i][0] != 31:
            res.append((i, *height[i]))

    print(len(res))
    while res:
        print(*res.pop())





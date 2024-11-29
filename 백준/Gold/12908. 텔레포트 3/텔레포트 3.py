import sys
input = sys.stdin.readline
INF = 10**6
xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

def getDist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)
t = []
res = -1
for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    t.append((x1, y1, x2, y2))
    t.append((x2, y2, x1, y1))

for i in range(7):
    for j in range(7):
        for k in range(7):
            td = 0
            tx, ty = xs, ys
            if i != 6:
                td += getDist(tx, ty, t[i][0], t[i][1]) + 10
                tx, ty = t[i][2], t[i][3]
            if j != 6:
                td += getDist(tx, ty, t[j][0], t[j][1]) + 10
                tx, ty = t[j][2], t[j][3]
            if k != 6:
                td += getDist(tx, ty, t[k][0], t[k][1]) + 10
                tx, ty = t[k][2], t[k][3]
            td += getDist(tx, ty, xe, ye)
            if res == -1 or td < res:
                res = td

print(res)




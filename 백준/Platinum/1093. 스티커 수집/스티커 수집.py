import sys

INF = 10**9+7
input = sys.stdin.readline


N = int(input().strip())
cost = list(map(int, input().split()))
value = list(map(int, input().split()))
K = int(input().strip())
T = int(input().strip())
tmp = [1]*N
if T != 0:
    for i in map(int, input().split()):
        tmp[i] = 0
size = N//2
ac, bc = cost[:size], cost[size:]
av, bv = value[:size], value[size:]
c1 = []
for i in range(1 << size):
    mask = 0
    sc = 0
    sv = 0
    while mask < size:
        if i & (1 << mask):
            sc += ac[mask]*tmp[mask]
            sv += av[mask]
        elif not tmp[mask]:
            sc -= ac[mask]
        mask += 1
    c1.append((sv, sc))
c2 = []
for i in range(1 << (N-size)):
    mask = 0
    sc = 0
    sv = 0
    while mask < (N-size):
        if i & (1 << mask):
            sc += bc[mask] * tmp[size+mask]
            sv += bv[mask]
        elif not tmp[size+mask]:
            sc -= bc[mask]
        mask += 1
    c2.append((sv, sc))

c1.sort()
c2.sort(reverse=True)
c2.append((-INF, 0))
r = 0
r_min = INF
res = INF
for lv, lc in c1:
    while True:
        if lv+c2[r][0] >= K:
            r_min = min(c2[r][1], r_min)
            r += 1
        else:
            break
    res = min(res, lc+r_min)

if r_min == INF:
    print(-1)
else:
    print(max(0, res))

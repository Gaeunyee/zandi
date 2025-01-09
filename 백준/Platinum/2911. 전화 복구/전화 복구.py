import sys
input = sys.stdin.readline

N, M = map(int, input().split())
detector = [(-1, 0), (M, 0)]
for _ in range(N):
    detector.append(tuple(map(int, input().split())))

dst = sorted(detector, key=lambda x: x[0])
block = [i for i in range(N+2)]
call = []
for idx in range(N+2):
    call.append((idx,)+dst[idx])
call.sort(key=lambda x: x[2])
area = 1
res, tr, buffer = 0, 0, 0
for i in range(2, N+2):
    idx, d, p = call[i]
    if p > tr:
        area += buffer
        buffer = 0
        res += (p-tr)*area
        tr = p
    buffer += 1
    if dst[idx-1][1] <= p:
        buffer -= 1
    if dst[idx+1][1] < p:
        buffer -= 1
print(res)


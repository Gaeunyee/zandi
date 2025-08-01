import sys
input = sys.stdin.readline

N, B, W = map(int, input().split())
lst = input().strip()

r = 0
b, w = 0, 0
res = 0
for l in range(N):
    while (r < N) and b + (1 if lst[r] == 'B' else 0) <= B:
        if lst[r] == 'W':
            w += 1
        else:
            b += 1
        r += 1
    if w >= W:
        res = max(res, r-l)
    if lst[l] == 'W':
        w -= 1
    else:
        b -= 1

print(res)

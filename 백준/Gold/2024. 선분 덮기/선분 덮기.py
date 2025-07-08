import sys
input = sys.stdin.readline

def solve(M):
    lines = []
    end = -1
    while True:
        u, v = map(int, input().split())
        if u == v == 0:
            break
        if u <= 0:
            end = max(end, v)
        else:
            lines.append((u, v))
    lines.sort()
    lines.append((10**6, 10**6))
    buffer = -1
    cost = 1
    f = 1 if end >= M else 0
    if f:
        print(1)
        return
    for s, e in lines:
        if end >= s:
           buffer = max(buffer, e)
        else:
            if buffer > end:
                cost += 1
                end = buffer
                buffer = -1
                if end >= M:
                    f = 1
                    break
            if end >= s:
                buffer = max(buffer, e)
            else:
                break
    print(cost if f else 0)


while True:
    N = input().strip()
    if N:
        solve(int(N))
    else:
        break


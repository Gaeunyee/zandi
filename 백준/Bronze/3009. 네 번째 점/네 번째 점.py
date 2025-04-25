import sys
input = sys.stdin.readline


x, y = {}, {}
for _ in range(3):
    u, v = map(int, input().split())
    if u not in x:
        x[u] = 0
    if v not in y:
        y[v] = 0
    x[u] += 1
    y[v] += 1

for i, s in x.items():
    if s == 1:
        print(i, end=' ')
for i, s in y.items():
    if s == 1:
        print(i)


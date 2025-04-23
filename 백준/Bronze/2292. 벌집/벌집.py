import sys
input = sys.stdin.readline


N = int(input().strip())
r = 1
c = 6
s = 1
if N == 1:
    print(1)
    exit()
while s < N:
    r += 1
    s += c
    c += 6

print(r)

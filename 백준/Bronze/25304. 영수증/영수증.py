import sys
input = sys.stdin.readline

X = int(input().strip())
N = int(input().strip())
c = 0
for _ in range(N):
    u, v = map(int, input().split())
    c += u*v

if c == X:
    print('Yes')
else:
    print('No')


import sys
input = sys.stdin.readline

N = int(input().strip())
S = 0
a = int('1'*21, 2)
for _ in range(N):
    c, *x = input().split()
    if len(x) == 1:
        x = int(x[0])
    if c == 'add':
        S |= (1 << x)
    elif c == 'remove':
        S &= a ^ (1 << x)
    elif c == 'check':
        if S & (1 << x):
            print(1)
        else:
            print(0)
    elif c == 'toggle':
        S ^= 1 << x
    elif c == 'all':
        S = a
    else:
        S = 0



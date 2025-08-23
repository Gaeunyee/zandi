import sys
input = sys.stdin.readline

N = int(input())
lst = map(int, input().split())
xor = 0
s = 0
for i in lst:
    xor ^= i
    s += i

if s == N:
    print('koosaga' if s % 2 == 0 else 'cubelover')
else:
    print('koosaga' if xor else 'cubelover')


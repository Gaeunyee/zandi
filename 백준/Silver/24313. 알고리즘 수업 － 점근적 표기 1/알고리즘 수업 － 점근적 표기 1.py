import sys
input = sys.stdin.readline


a1, a2 = map(int, input().split())
c = int(input().strip())
n = int(input().strip())
if c >= a1 and a1*n+a2 <= c*n:
    print(1)
else:
    print(0)
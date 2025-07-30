import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a, b, x = map(int, input().split())
    print(a*(x-1)+b)



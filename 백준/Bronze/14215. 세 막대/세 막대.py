import sys
input = sys.stdin.readline


a, b, c = map(int, input().split())
print(min(a+b+c-max(a, b, c)-1, max(a, b, c))+a+b+c-max(a, b, c))


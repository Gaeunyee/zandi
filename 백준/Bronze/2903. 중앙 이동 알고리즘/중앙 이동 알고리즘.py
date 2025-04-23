import sys
input = sys.stdin.readline


N = int(input().strip())
print(((1 << N) + 1) ** 2)


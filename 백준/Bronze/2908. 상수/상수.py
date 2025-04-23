import sys
input = sys.stdin.readline


A, B = input().split()
print(max(A[::-1], B[::-1]))



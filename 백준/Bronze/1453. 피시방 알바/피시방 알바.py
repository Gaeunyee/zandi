import sys
from math import ceil, log
input = sys.stdin.readline

N = int(input())
lst = set(map(int, input().split()))
print(N-len(lst))
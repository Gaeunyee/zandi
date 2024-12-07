import sys
import heapq as hq
input = sys.stdin.readline


while True:
    a, b, c = map(int, input().split())
    if a == b == c:
        break
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        print("right")
    else:
        print("wrong")
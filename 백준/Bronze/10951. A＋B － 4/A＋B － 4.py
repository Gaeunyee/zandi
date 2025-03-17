import sys
input = sys.stdin.readline

while True:
    IN = input().split()
    if not IN:
        break
    A, B = map(int, IN)
    print(A+B)

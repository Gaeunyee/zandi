import sys
input = sys.stdin.readline


while True:
    a, b, c = map(int, input().split())
    s = {a, b, c}
    l = max(a, b, c)
    if a == b == c == 0:
        break
    if a+b+c <= 2*l:
        print("Invalid")
    else:
        if len(s) == 3:
            print("Scalene")
        elif len(s) == 2:
            print("Isosceles")
        else:
            print("Equilateral")

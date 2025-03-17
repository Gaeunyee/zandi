import sys
input = sys.stdin.readline

y = int(input().strip())

if y % 4 == 0 and y % 100 != 0:
    print(1)
elif y % 400 == 0:
    print(1)
else:
    print(0)


import sys
input = sys.stdin.readline

while True:
    N = input().strip()
    if N == '0':
        break
    res = 0
    for i in N:
        if i == '1':
            res += 2
        elif i == '0':
            res += 4
        else:
            res += 3
    print(res+len(N)+1)
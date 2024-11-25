import sys
input = sys.stdin.readline

N = int(input().strip())

for a in range(1, 5000):
    for b in range(-5000, 5000):
        if a != 0 and b != 0 and N%a == 0 and (N+2)%b == 0:
            c, d = N//a, -(N+2)//b
            if a * c == N and b * d == -(N + 2) and a * d + b * c == N + 1:
                print(a, b, c, d)
                exit()

print(-1)

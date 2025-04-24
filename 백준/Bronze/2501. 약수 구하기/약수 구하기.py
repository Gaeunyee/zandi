import sys
input = sys.stdin.readline



N, K = map(int, input().split())
c = 0
for i in range(1, N+1):
    if N % i == 0:
        c += 1
        if c == K:
            print(i)
            exit()

print(0)
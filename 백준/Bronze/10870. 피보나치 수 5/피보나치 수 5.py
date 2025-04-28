import sys

input = sys.stdin.readline


N = int(input().strip())
fibo = [0]*(30)
fibo[0], fibo[1] = 0, 1
for i in range(2, N+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[N])


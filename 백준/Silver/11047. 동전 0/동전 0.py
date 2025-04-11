import sys
input = sys.stdin.readline


N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input().strip()))

res = 0
for i in reversed(coins):
    res += K//i
    K %= i

print(res)

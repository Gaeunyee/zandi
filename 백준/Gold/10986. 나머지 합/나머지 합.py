import sys
input = sys.stdin.readline


N, M = map(int, input().split())

lst = list(map(int, input().split()))
r = [0]*M
r[0] = 1
s = 0
for i in range(N):
    s += lst[i]
    s %= M
    r[s] += 1

res = 0
for i in range(M):
    res += r[i]*(r[i]-1)//2

print(res)






import sys
input = sys.stdin.readline

N = int(input().strip())
lst = list(map(int, input().split()))
res = 10**9+7

for i in range(1, N):
    lst[i] += lst[i-1]

lst = [(lst[i], i+1) for i in range(N)]
lst.append((0, 0))
lst.sort()
u, v = -1, -1
for i in range(N):
    a, b = lst[i][1], lst[i+1][1]
    if a > b:
        a, b = b, a
        t = lst[i][0] - lst[i+1][0]
        if abs(res) > abs(t):
            res = t
            u, v = a+1, b
    else:
        t = lst[i+1][0] - lst[i][0]
        if abs(res) > abs(t):
            res = t
            u, v = a+1, b


print(res)
print(u, v)




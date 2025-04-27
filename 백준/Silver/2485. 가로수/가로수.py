import sys
input = sys.stdin.readline
m = 10**9 + 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    while True:
        if b == 0:
            return a
        a, b = b, a % b


N = int(input().strip())
lst = []
for _ in range(N):
    lst.append(int(input().strip()))
c = lst[1]-lst[0]

for i in range(1, N-1):
    c = gcd(lst[i+1]-lst[i], c)

res = 0
for i in range(N-1):
    res += (lst[i+1]-lst[i])//c - 1

print(res)



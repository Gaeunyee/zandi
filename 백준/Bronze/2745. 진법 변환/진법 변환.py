import sys
input = sys.stdin.readline


n, b = input().split()
n = n[::-1]
b = int(b)

def change(n):
    if ord(n) >= 65:
        return ord(n) - 55
    return int(n)


res = 0
for i in range(len(n)):
    res += change(n[i])*b**i

print(res)
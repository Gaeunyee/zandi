import sys
input = sys.stdin.readline


n, b = map(int, input().split())

def change(n):
    if n < 10:
        return str(n)
    return chr(n+55)


res = ''
while n != 0:
    res = change(n % b) + res
    n //= b

print(res)
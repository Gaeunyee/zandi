import sys

input = sys.stdin.readline


s = ['-']
for i in range(1, 13):
    s.append(s[-1]+' '*(3**(i-1))+s[-1])

while True:
    n = input().strip()
    if not n:
        break
    print(s[int(n)])

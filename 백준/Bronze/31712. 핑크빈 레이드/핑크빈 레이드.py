import sys
input = sys.stdin.readline

l, r = 0, 10**9+7
lst = []
s = 0
for _ in range(3):
    c, u = map(int, input().split())
    s += u
    lst.append((c, u))

H = int(input().strip())
H -= s
if H <= 0:
    print(0)
    exit()
while l+1 < r:
    m = (l+r)//2
    atk = 0
    for c, d in lst:
        atk += (m//c)*d
    if atk >= H:
        r = m
    else:
        l = m
print(r)
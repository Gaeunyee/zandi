import sys
input = sys.stdin.readline

N = int(input().strip())
lst = []
cnt = [0]*8005
for _ in range(N):
    a = int(input().strip())
    lst.append(a)
    cnt[a] += 1

avg = sum(lst)/N
if avg >= 0:
    print(int(avg)+1 if int(avg+0.5) > int(avg) else int(avg))
else:
    print(int(avg)-1 if int(avg-0.5) < int(avg) else int(avg))
l = set(lst)
lst.sort()
print(lst[N//2])
c = -1
r = -1
s = 0
for i in sorted(l):
    if c < cnt[i]:
        r = i
        c = cnt[i]
        s = 1
    elif c == cnt[i] and s == 1:
        r = i
        s += 1
print(r)
print(max(lst)-min(lst))


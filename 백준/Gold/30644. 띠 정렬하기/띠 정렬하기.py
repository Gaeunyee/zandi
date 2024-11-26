import sys
input = sys.stdin.readline

N = int(input().strip())
lst = list(map(int, input().split()))
lst2 = list(enumerate(lst))
lst2.sort(key=lambda x: x[1])
l = []
i = 0
for idx, size in lst2:
    l.append((idx, i))
    i += 1

l.sort()
p, i = 0, 1
cnt = 0
while i < N:
    if l[i][1] - l[p][1] == 1 or l[i][1] - l[p][1] == -1:
        p += 1
        i += 1
    else:
        cnt += 1
        p = i
        i = p+1

print(cnt)


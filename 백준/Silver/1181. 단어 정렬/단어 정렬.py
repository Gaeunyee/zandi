import sys
input = sys.stdin.readline


N = int(input().strip())
sets = set()
lst = []
for i in range(N):
    sets.add(input().strip())
for s in sets:
    lst.append((len(s), s))

lst.sort()
for l, s in lst:
    print(s)


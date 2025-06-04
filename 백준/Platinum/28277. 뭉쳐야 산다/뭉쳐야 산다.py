import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
sets = [set()]
for _ in range(N):
    n, *s = map(int, input().split())
    sets.append(set(s))


def union(x, y):
    if len(sets[x]) < len(sets[y]):
        sets[x], sets[y] = sets[y], sets[x]
    sets[x] |= sets[y]
    sets[y] = set()


for _ in range(Q):
    c, *x = map(int, input().split())
    if c == 1:
        union(x[0], x[1])
    else:
        print(len(sets[x[0]]))


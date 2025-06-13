import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


G = int(input().strip())
P = int(input().strip())

lst = []
for _ in range(P):
    lst.append(int(input().strip()))
par = [-1]*(G+2)
used = [0]*(G+2)

def find(x):
    if par[x] < 0:
        return x
    par[x] = find(par[x])
    return par[x]

def union(a, b):
    x, y = find(a), find(b)
    if x == y:
        return False
    if x > y:
        x, y = y, x
    par[x] += par[y]
    par[y] = x
    return True


res = 0
for i in range(P):
    t = find(lst[i])
    t -= used[t]
    if t == 0:
        break
    res += 1
    used[t] = 1
    if used[t+1]:
        union(t, t+1)
    if used[t-1]:
        union(t-1, t)

print(res)


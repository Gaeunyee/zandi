import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, Q = map(int, input().split())
parent = [i for i in range(N+1)]
graph = [0, 0]
for _ in range(N-1):
    graph.append(int(input().strip()))


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    x, y = find(a), find(b)
    if x == y:
        return False
    parent[y] = x
    return True

query = []
for _ in range(N+Q-1):
    query.append(tuple(map(int, input().split())))

ans = []
for c, *a in reversed(query):
    if c == 0:
        union(a[0], graph[a[0]])
    else:
        ans.append(1 if find(a[0]) == find(a[1]) else 0)

for i in reversed(ans):
    print('YES' if i else 'NO')


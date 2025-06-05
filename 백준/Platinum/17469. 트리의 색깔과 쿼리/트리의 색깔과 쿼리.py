import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, Q = map(int, input().split())
sets = [set() for _ in range(N+1)]
parent = [i for i in range(N+1)]
graph = [0, 0]
for _ in range(N-1):
    graph.append(int(input().strip()))

for i in range(1, N+1):
    sets[i].add(int(input().strip()))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    x, y = find(a), find(b)
    if x == y:
        return False
    if len(sets[x]) < len(sets[y]):
        sets[x], sets[y] = sets[y], sets[x]
    sets[x] |= sets[y]
    sets[y] = set()
    parent[y] = x
    return True

query = []
for _ in range(N+Q-1):
    query.append(tuple(map(int, input().split())))

ans = []
for c, a in reversed(query):
    if c == 1:
        union(a, graph[a])
    else:
        ans.append(len(sets[find(a)]))

for i in reversed(ans):
    print(i)


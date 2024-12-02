import sys
input = sys.stdin.readline
INF = 10**6
sys.setrecursionlimit(10**5)
N = int(input().strip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y, l = map(int, input().split())
    graph[x].append((y, l))
    graph[y].append((x, l))


def dfs(node, depth):
    global max_depth, max_node
    visited[node] = True
    if depth > max_depth:
        max_depth = depth
        max_node = node
    for next, l in graph[node]:
        if not visited[next]:
            dfs(next, depth+l)

def makeTable(node, depth, table):
    table[node] = depth
    for next, l in graph[node]:
        if table[next] == -1:
            makeTable(next, depth+l, table)

visited = [False]*(N+1)
max_depth, max_node = 0, 0
dfs(1, 0)
found1 = max_node

visited = [False]*(N+1)
max_depth, max_node = 0, 0
dfs(found1, 0)
found2 = max_node

table1 = [-1]*(N+1)
table2 = [-1]*(N+1)
makeTable(found1, 0, table1)
makeTable(found2, 0, table2)

for i in range(1, N+1):
    print(max(table1[i], table2[i]))


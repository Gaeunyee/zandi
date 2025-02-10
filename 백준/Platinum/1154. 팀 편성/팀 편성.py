import sys
input = sys.stdin.readline

N = int(input().strip())
graph = [{i} for i in range(N+1)]
ex_graph = [{}]

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a].add(b)
    graph[b].add(a)

U = {i for i in range(1, N+1)}
for i in range(1, N+1):
    ex_graph.append(U-graph[i])

team = [0]*(N+1)
group = [[], [], []]
def dfs(v, t):
    if team[v]:
        if t == team[v]:
            return
        else:
            print(-1)
            exit()
    team[v] = t
    group[t].append(v)
    for next in ex_graph[v]:
        dfs(next, -t)


for i in range(1, N+1):
    if not team[i]:
        dfs(i, 1)
print(1)
print(*sorted(group[1]), -1)
print(*sorted(group[-1]), -1)


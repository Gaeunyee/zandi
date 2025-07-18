import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5 + 3)
def SCC(u, low):
    global time, SCCs
    low[u] = time
    discovery[u] = time
    time += 1
    stack.append(u)


    for v in graph[u]:
        if low[v] == -1:
            SCC(v, low)
            low[u] = min(low[u], low[v])
        elif visited[v] == -1:
            low[u] = min(low[u], low[v])

    if low[u] == discovery[u]:
        current_scc = []
        while stack:
            w = stack.pop()
            visited[w] = len(SCCs)
            current_scc.append(w)
            if w == u:
                break
        SCCs.append(current_scc)


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]
    low = [-1] * (V + 1)
    stack = []
    visited = [-1] * (V + 1)
    discovery = [-1] * (V + 1)
    time = 0
    SCCs = []

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    if t != T-1:
        input()

    for i in range(V):
        if low[i] == -1:
            SCC(i, low)

    deg = [0] * len(SCCs)
    acc = [-1] * len(SCCs)
    new_graph = [[] for _ in range(len(SCCs))]
    for scc in SCCs:
        for i in scc:
            for j in graph[i]:
                if visited[i] != visited[j] and acc[visited[j]] != visited[i]:
                    acc[visited[j]] = visited[i]
                    new_graph[visited[i]].append(visited[j])
                    deg[visited[j]] += 1

    res = -1
    for i in range(len(SCCs)):
        if deg[i] == 0:
            if res == -1:
                res = i
            else:
                res = -2
                break

    if res >= 0:
        for i in sorted(SCCs[res]):
            print(i)
        if t != T - 1:
            print()
    else:
        print('Confused')
        if t != T - 1:
            print()

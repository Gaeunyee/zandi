import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)
def SCC(u):
    global time, bottom
    low[u] = time
    discovery[u] = time
    time += 1
    stack.append(u)


    for v in graph[u]:
        if low[v] == -1:  # 방문하지 않은 노드인 경우
            SCC(v)
            low[u] = min(low[u], low[v])
        elif not visited[v]:  # 스택에 있는 노드인 경우
            low[u] = min(low[u], low[v])

    if low[u] == discovery[u]:  # SCC 루트 발견
        inSCC = [0]*(N+1)
        current_scc = []
        while stack:
            w = stack.pop()
            visited[w] = True
            inSCC[w] = 1
            current_scc.append(w)
            if w == u:
                break
        for t in current_scc:
            for v in graph[t]:
                if not inSCC[v]:
                    return
        bottom += current_scc

while True:
    K = input().split()
    if K == ['0']:
        break
    N, M = map(int, K)
    graph = [[] for i in range(N+1)]
    edge = list(map(int, input().split()))
    for i in range(M):
        graph[edge[2*i]].append(edge[2*i+1])
    low = [-1] * (N*2+1)
    stack = []
    visited = [False]*(N*2+1)
    discovery = [-1]*(N*2+1)
    time = 0
    bottom = []

    for i in range(1, N+1):
        if low[i] == -1:
            SCC(i)
    print(*sorted(bottom))

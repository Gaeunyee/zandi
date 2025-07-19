import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit((10**5) * 5 + 1)
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
        flag = -1
        m = 0
        while stack:
            w = stack.pop()
            if isRes[w]:
                flag = -2
            m += money[w]
            visited[w] = len(SCCs)
            current_scc.append(w)
            if w == u:
                break
        current_scc.append(flag)
        current_scc.append(m)
        SCCs.append(current_scc)


T = 1
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
    money = [0]
    for _ in range(V):
        money.append(int(input()))
    S, P = map(int, input().split())
    isRes = [0]*(V+1)
    for i in map(int, input().split()):
        isRes[i] = 1

    for i in range(1, V+1):
        if low[i] == -1:
            SCC(i, low)
            
    del low, stack, discovery
    
    deg = [0] * len(SCCs)
    acc = [-1] * len(SCCs)
    new_graph = [[] for _ in range(len(SCCs))]
    new_money = [0]*len(SCCs)
    qu = deque([visited[S]])
    isRes = [0]*(len(SCCs))
    new_money[visited[S]] = 1


    for s in range(len(SCCs)):
        scc = SCCs[s]
        isRes[s] = scc[-2]
        new_money[s] = scc[-1]
        for i in scc[:-2]:
            for j in graph[i]:
                if visited[i] != visited[j] and acc[visited[j]] != visited[i]:
                    acc[visited[j]] = visited[i]
                    new_graph[visited[i]].append(visited[j])
                    
    del graph
    
    isRes[visited[S]] *= -1
    while qu:
        t = qu.popleft()
        for n in new_graph[t]:
            deg[n] += 1
            if isRes[n] < 0:
                isRes[n] *= -1
                qu.append(n)


    qu = deque()
    qu.append(visited[S])
    dp = [0]*(len(SCCs))
    dp[visited[S]] = new_money[visited[S]]
    res = -1
    while qu:
        t = qu.popleft()
        if isRes[t] == 2:
            res = max(res, dp[t])
        for n in new_graph[t]:
            dp[n] = max(dp[n], dp[t]+new_money[n])
            deg[n] -= 1
            if not deg[n]:
                qu.append(n)

    print(res)

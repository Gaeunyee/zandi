import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
id = 0
def SCC(u, low):
    global time, SCCs, id
    low[u] = time
    discovery[u] = time
    time += 1
    stack.append(u)


    for v in graph[u]:
        if low[v] == -1:  # 방문하지 않은 노드인 경우
            SCC(v, low)
            low[u] = min(low[u], low[v])
        elif not visited[v]:  # 스택에 있는 노드인 경우
            low[u] = min(low[u], low[v])

    if low[u] == discovery[u]:
        id += 1 # SCC 루트 발견
        current_scc = []
        while stack:
            w = stack.pop()
            visited[w] = True
            SCC_id[w] = id
            current_scc.append(w)

            if w == u:
                break
        SCCs.append(current_scc)


N, M = map(int, input().split())
graph = [[] for i in range(N*2+1)]
low = [-1] * (N*2+1)
stack = []
visited = [False]*(N*2+1)
discovery = [-1]*(N*2+1)
time = 0
SCCs = []
flag = True
SCC_id = [-1]*(N*2+1)
for _ in range(M):
    n1, c1, n2, c2, n3, c3 = input().split()
    n = list(map(int, [n1, n2, n3]))  # R : +, B : -
    c = list(map(lambda x: 1 if x == 'R' else -1, [c1, c2, c3]))
    graph[-c[0]*n[0]].append(c[1]*n[1])
    graph[-c[0]*n[0]].append(c[2]*n[2])
    graph[-c[1]*n[1]].append(c[0]*n[0])
    graph[-c[1]*n[1]].append(c[2]*n[2])
    graph[-c[2]*n[2]].append(c[0]*n[0])
    graph[-c[2]*n[2]].append(c[1]*n[1])

for i in range(1, N*2+1):
    if low[i] == -1:
        if i > N:
            SCC(i-(N*2+1), low)
        else:
            SCC(i, low)

for i in range(1, N+1):
    if SCC_id[i] == SCC_id[-i]:
        print(-1)
        flag = False
        exit()

table = [-1]*(N+1)
if flag:
    for idx in range(len(SCCs) - 1, -1, -1):
        for t in SCCs[idx]:
            if table[abs(t)] == -1:
                if t < 0:
                    table[-t] = 1
                else:
                    table[t] = 0

for i in range(1, N+1):
    print('R' if table[i] > 0 else 'B', end='')
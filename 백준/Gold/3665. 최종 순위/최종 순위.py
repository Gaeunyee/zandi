import sys
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    lst = list(map(int, input().split()))
    graph = [[0]*(N+1) for _ in range(N+1)]
    deg = [0]*(N+1)
    for i in range(N):
        for j in range(i+1, N):
            graph[lst[i]][lst[j]] = 1
            deg[lst[j]] += 1
    M = int(input().strip())
    for _ in range(M):
        a, b = map(int, input().split())
        if graph[a][b] == 1:
            deg[b] -= 1
            deg[a] += 1
        else:
            deg[a] -= 1
            deg[b] += 1
        graph[a][b], graph[b][a] = graph[b][a], graph[a][b]

    qu = []
    res = []
    for i in range(1, N+1):
        if deg[i] == 0:
            qu.append(i)
            res.append(i)

    f = 1

    while qu:
        if len(qu) > 1:
            f = -1  # ?
            break
        t = qu.pop()
        for i in range(1, N+1):
            if graph[t][i]:
                deg[i] -= 1
                if deg[i] == 0:
                    qu.append(i)
                    res.append(i)

    if f == -1:
        print("?")
    elif sum(deg):
        print("IMPOSSIBLE")
    else:
        print(*res)

T = int(input().strip())
for _ in range(T):
    solve()

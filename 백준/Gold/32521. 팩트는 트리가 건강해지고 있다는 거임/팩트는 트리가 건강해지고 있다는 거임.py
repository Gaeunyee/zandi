import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+7)

N, K = map(int, input().split())
gungang = [0]+list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
res = 0
def dfs(t):
    global res
    visited[t] = 1
    st = [gungang[t]]
    for nxt in graph[t]:
        if not visited[nxt]:
            st.append(dfs(nxt))
    s = sum(st)
    if s > K:
        st.sort(reverse=True)
        for i in st:
            s -= i
            res += 1
            if s <= K:
                break
    return s

dfs(1)
print(res)



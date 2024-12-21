import sys
from collections import deque
input = sys.stdin.readline


N = int(input().strip())
hash = ' ' + input().strip()
graph = [[] for i in range(N+1)]
for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

par = [-1]*(N+1)
par[1] = 0
def bfs(t):
    qu = deque()
    qu.append(1)
    st = []
    h = 0
    node = -1
    while True:
        if not qu and st:
            while st:
                qu.append(st.pop())
            h = 0
        elif not qu and not st:
            break
        node = qu.popleft()
        for nxt in graph[node]:
            if par[nxt] == -1:
                par[nxt] = node
                if hash[h] == hash[nxt]:
                    st.append(nxt)
                elif hash[h] < hash[nxt]:
                    st = []
                    h = nxt
                    st.append(nxt)
    tr = node
    ret = []
    while tr != 0:
        ret.append(tr)
        tr = par[tr]
    while ret:
        print(hash[ret.pop()], end='')


bfs(1)


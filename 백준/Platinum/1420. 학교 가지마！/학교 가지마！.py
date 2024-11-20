import sys
from collections import deque
input = sys.stdin.readline
INF = 10**5

class Edge:
    def __init__(self, cap, s, e, l, r):
        self.capacity = cap
        self.flow = 0
        self.rvs = None
        self.ix, self.iy = s, e
        self.ox, self.oy = l, r


N, M = map(int, input().split())
size = 210
graph = [[[] for _ in range(size)] for _ in range(size)]

for i in range(1, N+1):
    for j in range(1, M+1):
        c, r = Edge(1, -i, -j, i, j), Edge(0, i, j, -i, -j)
        c.rvs, r.rvs = r, c
        graph[-i][-j].append(c)
        graph[i][j].append(r)


table = ['']
for _ in range(N):  # end : - , start : +
    table.append('_'+input().strip())

dxdy = [(1, 0), (0, 1)]
sx, sy, ex, ey = -1, -1, -1, -1
for i in range(1, N+1):
    for j in range(1, M+1):
        if table[i][j] == 'K':
            sx, sy = (-i, -j)
        elif table[i][j] == 'H':
            ex, ey = (-i, -j)
        elif table[i][j] == '#':
            continue
        for dx, dy in dxdy:
            nx, ny = i+dx, j+dy
            if 1 <= nx <= N and 1 <= ny <= M and table[nx][ny] != '#':
                c, r = Edge(INF, i, j, -nx, -ny), Edge(0, -nx, -ny, i, j)
                c.rvs, r.rvs = r, c
                graph[i][j].append(c)
                graph[-nx][-ny].append(r)
                c, r = Edge(INF, nx, ny, -i, -j), Edge(0, -i, -j, nx, ny)
                c.rvs, r.rvs = r, c
                graph[nx][ny].append(c)
                graph[-i][-j].append(r)

graph[sx][sy][0].capacity = INF
while True:
    qu = deque()
    qu.append((sx, sy))
    par = [[None]*size for _ in range(size)]

    while qu and par[ex][ey] is None:
        tx, ty = qu.popleft()
        for edge in graph[tx][ty]:
            if (edge.capacity - edge.flow > 0
                    and par[edge.ox][edge.oy] is None):
                par[edge.ox][edge.oy] = edge
                qu.append((edge.ox, edge.oy))


    if par[ex][ey] is None:
        break
    end = (ex, ey)
    amount = INF
    if par[ex][ey].ix == -sx and par[ex][ey].iy == -sy:
        print(-1)
        exit()
    while end != (sx, sy):
        amount = min(amount, par[end[0]][end[1]].capacity - par[end[0]][end[1]].flow)
        end = par[end[0]][end[1]].ix, par[end[0]][end[1]].iy
    end = (ex, ey)
    while end != (sx, sy):
        par[end[0]][end[1]].flow += amount
        par[end[0]][end[1]].rvs.flow -= amount
        end = par[end[0]][end[1]].ix, par[end[0]][end[1]].iy

print(graph[sx][sy][0].flow)

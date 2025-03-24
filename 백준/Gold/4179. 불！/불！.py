import sys
from collections import deque
input = sys.stdin.readline

INF = 10 ** 6

def solve():
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    R, C = map(int, input().split())

    graph = []
    F = deque()
    J = deque()
    for i in range(R):
        l = list(input().strip())
        for j in range(C):
            if l[j] == 'J':
                J.append((0, i, j))
                l[j] = '.'
            if l[j] == 'F':
                F.append((0, i, j))
        graph.append(l)

    visited = [[0]*C for _ in range(R)]
    f = 0

    while J:
        t, x, y = J.popleft()
        if f < t:
            while F:
                if F[0][0] > t:
                    f = F[0][0]-1
                    break
                ft, fx, fy = F.popleft()
                for dx, dy in dxdy:
                    nx, ny = fx + dx, fy + dy
                    if 0 <= nx < R and 0 <= ny < C:
                        if graph[nx][ny] == '.':
                            graph[nx][ny] = 'F'
                            F.append((t+1, nx, ny))
        if graph[x][y] != '.':
            continue
        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            print(t + 1)
            return
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.' and (not visited[nx][ny]):
                    visited[nx][ny] = 1
                    J.append((t+1, nx, ny))
    print("IMPOSSIBLE")


solve()



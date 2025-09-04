import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dots = []
start = (0, 0)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dots.append((i, j))
        elif graph[i][j] == 2:
            start = i, j
dots.append(start)
edge = []
f = 1
for i in range(1, len(dots)):
    if (abs(dots[i][0]-dots[0][0]) + abs(dots[i][1]-dots[0][1]))%2:
        f = 0
        break

if not f:
    print('Shorei')
    exit()

visited = [0]*len(dots)
cnt = 0
t = 0
res = 10**9
def dfs(x):
    global t, cnt, res
    if t > res:
        return
    visited[x] = 1
    cnt += 1
    if cnt == len(dots):
        res = t
        visited[x] = 0
        cnt -= 1
        return
    for i in range(len(dots)):
        if not visited[i]:
            t += max(abs(dots[i][0] - dots[x][0]), abs(dots[i][1] - dots[x][1]))
            dfs(i)
            t -= max(abs(dots[i][0] - dots[x][0]), abs(dots[i][1] - dots[x][1]))
    visited[x] = 0
    cnt -= 1

dfs(-1)
print('Undertaker')
print(res)
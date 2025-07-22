import sys
input = sys.stdin.readline
id = 0

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dp_l = [0]*M
dp_r = [0]*M
dp_l[0], dp_r[0] = graph[0][0], graph[0][0]

for i in range(1, M):
    dp_l[i], dp_r[i] = dp_l[i-1]+graph[0][i], dp_r[i-1]+graph[0][i]

for i in range(1, N):
    for j in range(M):
        dp_l[j] += graph[i][j]
        dp_r[j] += graph[i][j]

    for j in range(1, M):
        dp_l[j] = max(dp_l[j], dp_l[j-1]+graph[i][j])
    for j in range(M-2, -1, -1):
        dp_r[j] = max(dp_r[j], dp_r[j+1]+graph[i][j])

    for j in range(M):
        dp_l[j], dp_r[j] = max(dp_l[j], dp_r[j]), max(dp_l[j], dp_r[j])

print(dp_l[M-1])


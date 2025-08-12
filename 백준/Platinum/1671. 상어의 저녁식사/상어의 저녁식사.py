import sys
input = sys.stdin.readline


def matchinig(n):
    for e in edge[n]:
        if visited[e]:
            continue
        visited[e] = True
        if end[e] == -1 or matchinig(end[e]):
            end[e] = n
            return True
    return False


n = int(input())
end = [-1] * n
edge = [[] for _ in range(n + 1)]
lst = []
for _ in range(n):
    a, b, c = map(int, input().split())
    lst.append((a, b, c))
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if lst[i] == lst[j]:
            if i > j:
                continue
            edge[i].append(j)
        elif lst[i][0] >= lst[j][0] and lst[i][1] >= lst[j][1] and lst[i][2] >= lst[j][2]:
            edge[i].append(j)

cnt = 0
for i in range(n):
    visited = [False] * (n+1)
    if matchinig(i):
        cnt += 1
for i in range(n):
    visited = [False] * (n+1)
    if matchinig(i):
        cnt += 1
print(n-cnt)

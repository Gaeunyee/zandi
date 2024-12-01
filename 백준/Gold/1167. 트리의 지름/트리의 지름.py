import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input().strip())
lst = [[] for _ in range(N+1)]

max_depth = 0
max_node = 0


def dfs(tmp, d):
    global max_depth, max_node
    visited[tmp] = 1
    for next, l in lst[tmp]:
        if visited[next] == 0:
            dfs(next, d + l)
    if d > max_depth:
        max_depth = d
        max_node = tmp
    return d


for i in range(N):
    data = list(map(int, input().split()))
    for j in range(1, len(data)-2, 2):
        lst[data[0]].append((data[j], data[j+1])) # (위치, 거리)
        lst[data[j]].append((data[0], data[j+1]))

visited = [0]*(N+1)
dfs(1, 0)

max_depth = 0
visited = [0]*(N+1)
dfs(max_node, 0)
print(max_depth)
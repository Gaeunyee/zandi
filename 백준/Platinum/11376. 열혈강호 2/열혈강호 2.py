import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(1, N+1):
    c, *a = map(int, input().split())
    for k in a:
        graph[i].append(k)

visited = [False]*(N+1)


att = 0
right_pair = [0]*(M+1)
def bipMatching(cur):
    visited[cur] = True
    for pair in graph[cur]:
        if ((not right_pair[pair]) or
                ((not visited[right_pair[pair]]) and bipMatching(right_pair[pair]))):
                right_pair[pair] = cur
                return True
    return False


for i in range(1, N+1):
    visited = [False]*(N+1)
    if bipMatching(i):
        att += 1
for i in range(1, N+1):
    visited = [False]*(N+1)
    if bipMatching(i):
        att += 1
print(att)

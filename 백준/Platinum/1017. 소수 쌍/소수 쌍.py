import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N = int(input().strip())
graph = [[] for i in range(N+1)]
lst = list(map(int, input().split()))
primes = [1]*(2003)
for i in range(2, 46):
    for j in range(2, 2002//i):
        primes[i*j] = 0

for i in range(N):
    for j in range(i+1, N):
        u, v = i, j
        if primes[lst[i]+lst[j]]:
            if lst[i] % 2 != lst[0] % 2:
                u, v = j, i
            graph[u].append(v)



def bipMatching(cur):
    visited[cur] = True
    for pair in graph[cur]:
        if ((right_pair[pair] == -1) or
                ((not visited[right_pair[pair]]) and
                 bipMatching(right_pair[pair]))):
                right_pair[pair] = cur
                return True
    return False


res = []
for k in graph[0]:
    att = 1
    right_pair = [-1] * (N+1)
    right_pair[k] = 0
    for i in range(1, N):
        visited = [False]*(N+1)
        visited[0] = True
        if bipMatching(i):
            att += 1
    if att == N//2:
        res.append(lst[k])

if res:
    print(*sorted(res))
else:
    print(-1)


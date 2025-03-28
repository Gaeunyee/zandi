import sys
input = sys.stdin.readline

mod = 10**9 + 7
N, M = map(int, input().split())
arr = [0, 0] + list(map(int, input().split()))
graph = [[] for _ in range(N+2)]
res = 1
for _ in range(M):
    u, v, l, r = map(int, input().split())
    if arr[u] < arr[v]:
        u, v = v, u
    if arr[u]-arr[v] < l: # 적정 길이보다 긺
        res *= (r-l+1)
        res %= mod
    else:
        d = max(0, r-max(l, arr[u]-arr[v])+1)
        if d == 0:
            print(0)
            exit()
        graph[u].append(d)


for i in range(2, N+1):
    s, dec = 1, 1
    for j in graph[i]:
        s *= j
        dec *= j-1
        s %= mod
        dec %= mod
    res *= s-dec
    res %= mod


print(res)

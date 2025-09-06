import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
mod = 998244353

N = int(input())
par = [-1]+list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    graph[par[i]].append(i)

a = [-1]+list(map(int, input().split()))

for i in range(1, N+1):
    if par[i] == 0:
        R = i
        break
dp = [0]*(N+1)
dp[R] = 1

def dfs(x):
    global res
    ddfs(x, a[x], dp[x])
    for n in graph[x]:
        dfs(n)
    if not graph[x]:
        res += dp[x]
        res %= mod
res = 0
def ddfs(x, d, a):
    if d == 0:
        return
    for n in graph[x]:
        dp[n] += a
        dp[n] %= mod
        ddfs(n, d-1, a)


dfs(R)
print(res)


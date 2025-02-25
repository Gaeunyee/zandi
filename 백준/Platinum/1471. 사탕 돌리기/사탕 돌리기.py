import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)
INF = 10 ** 6

N = int(input().strip())
SIZE = N+1
dp = [-1]*SIZE
def func(num):
    ret = num
    while num != 0:
        ret += num % 10
        num //= 10
    r = ret % N
    return r if r else N

def dfs(node):
    global SIZE
    nxt = func(node)
    if node >= SIZE:
        return dfs(nxt)
    if dp[node] == -1:
        dp[node] = 0
        dfs(nxt)
        dp[node] = dp[nxt]+(1 if dp[node] == 0 else 0)
    elif dp[node] == 0:
        update(node, node, 1)
    return dp[node]



def update(start, node, m):
    next = func(node)
    if next == start:
        dp[node] = m
        return m
    dp[node] = update(start, next, m+1)
    return dp[node]
s = -1
for i in range(1, N+1):
    s = max(s, dfs(i))

print(s)



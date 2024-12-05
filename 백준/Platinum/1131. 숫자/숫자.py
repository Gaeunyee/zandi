import sys

input = sys.stdin.readline
INF = 10 ** 6

A, B, K = map(int, input().split())
SIZE = (9 ** K) * 6 + 7
dp = [-1]*SIZE
dp[1] = 1
def func(num):
    global K
    ret = 0
    while num != 0:
        ret += (num % 10) ** K
        num //= 10
    return ret

def dfs(node):
    global SIZE
    nxt = func(node)
    if node >= SIZE:
        return dfs(nxt)
    if dp[node] == -1:
        dp[node] = 0
        dfs(nxt)
        dp[node] = min(dp[nxt], node)
    elif dp[node] == 0:
        update(node, node, INF)
    return dp[node]



def update(start, node, m):
    next = func(node)
    if next == start:
        dp[node] = m
        return m
    dp[node] = update(start, next, min(m, node))
    return dp[node]
s = 0
for i in range(A, B+1):
    s += dfs(i)

print(s)



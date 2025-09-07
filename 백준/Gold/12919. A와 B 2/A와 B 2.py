import sys
input = sys.stdin.readline


S = input().strip()
T = input().strip()
res = 0
def dfs(l, r, rvs):
    global res
    if r-l+1 == len(S):
        if rvs == 1 and S == T[l:r+1]:
            res = 1
        elif rvs == -1 and S == T[r:l-1:-1]:
            res = 1
        return
    if rvs == 1:
        if T[r] == 'A':
            dfs(l, r-1, rvs)
        if T[l] == 'B':
            dfs(l+1, r, -rvs)
    else:
        if T[l] == 'A':
            dfs(l+1, r, rvs)
        if T[r] == 'B':
            dfs(l, r-1, -rvs)

dfs(0, len(T)-1, 1)
print(res)

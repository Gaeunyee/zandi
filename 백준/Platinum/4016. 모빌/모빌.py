import sys
sys.setrecursionlimit(10**5 + 3)
input = sys.stdin.readline

class Node:
    def __init__(self, l=-1, r=-1):
        self.left = l
        self.right = r
        self.d = 0



N = int(input().strip())
nodes = [Node() for _ in range(2*N+3)]

for i in range(1, N+1):
    u, v = map(int, input().split())
    nodes[i].left, nodes[i].right = u, v



def dfs(T, d):
    global max_d
    t = nodes[T]
    t.d = d
    if t.left != -1:
        dfs(t.left, d+1)
    if t.right != -1:
        dfs(t.right, d+1)


dfs(1, 0)
res = 0
def solve(T):
    global res
    t = nodes[T]
    if t.left != -1:
        l1, r1 = solve(t.left)
    else:
        l1, r1 = t.d+1, t.d+1
    if t.right != -1:
        l2, r2 = solve(t.right)
    else:
        l2, r2 = t.d+1, t.d+1

    if not (l1 >= r1 >= l2 >= r2):
        res += 1
        l1, r1, l2, r2 = l2, r2, l1, r1
    if not (l1 >= r1 >= l2 >= r2) or l1-r2 > 1:
        print(-1)
        exit()
    return l1, r2

solve(1)
print(res)


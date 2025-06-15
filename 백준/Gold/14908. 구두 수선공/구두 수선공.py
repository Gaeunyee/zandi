import sys
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    lst = []
    for i in range(1, N+1):
        t, s = map(int, input().split())
        lst.append((t, s, i))
    lst.sort(key=lambda x: x[1]/x[0], reverse=True)
    for i in range(N):
        print(lst[i][2], end=' ')
solve()


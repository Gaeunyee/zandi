import sys
input = sys.stdin.readline

INF = 10**9


def solve():
    N, M = map(int, input().split())
    for _ in range(M):
        input()
    print(N-1)


T = int(input().strip())
for _ in range(T):
    solve()

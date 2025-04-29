import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def move(n, s, e):
    if n == 1:
        print(s, e)
        return
    move(n-1, s, s ^ e)
    move(1, s, e)
    move(n-1, s ^ e, e)


N = int(input().strip())
print((1 << N)-1)
move(N, 1, 3)

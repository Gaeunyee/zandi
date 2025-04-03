import sys
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    res = 0
    for i in map(int, input().split()):
        res ^= i
    print("koosaga" if res != 0 else "cubelover")



solve()

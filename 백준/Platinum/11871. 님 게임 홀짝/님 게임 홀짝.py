import sys
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    res = 0
    for i in map(int, input().split()):
        if i % 2 == 0:
            res ^= i//2 - 1
        else:
            res ^= (i+1)//2
    print("koosaga" if res != 0 else "cubelover")



solve()

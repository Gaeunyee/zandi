import sys
input = sys.stdin.readline

def solve():
    SIZE = 3*(10**6) + 3
    fibo = [0]*35
    fibo[0], fibo[1] = 0, 1
    for i in range(2, 34):
        fibo[i] = fibo[i-1]+fibo[i-2]
    g = [-1]*SIZE
    g[0] = 0


    for n in range(1, SIZE):
        l = [0]*16
        t = n-1
        l[g[t]] = 1
        for j in range(1, 34):
            t -= fibo[j]
            if t < 0:
                break
            l[g[t]] = 1
        for i in range(16):
            if l[i] == 0:
                g[n] = i
                break


    N = int(input().strip())
    res = 0
    for i in map(int, input().split()):
        res ^= g[i]

    if res:
        print("koosaga")
    else:
        print("cubelover")

solve()

import sys
input = sys.stdin.readline


def makeSum(n):
    return (3*n*n + 3*n)//2

T = int(input().strip())
def solve():
    K = int(input().strip())
    l, r = 0, 10**5+7
    while l+1 < r:
        m = (l+r)//2
        if K > makeSum(m):
            l = m
        else:
            r = m
    R = K - makeSum(l)
    if R <= r:
        if r > 1:
            print(r, "dolphins")
        else:
            print(r, "dolphin")

    elif R <= 2*r:
        if r > 1:
            print(r, "jumps")
        else:
            print(r, "jump")

    else:
        print("splash")

for _ in range(T):
    solve()


import sys
input = sys.stdin.readline

INF = 10**9 + 7


def solve():
    L, N = map(int, input().split())
    lst = [[] for _ in range(N//2 + 1)]
    for _ in range(N):
        x, y, c = map(int, input().split())
        if x == 0:
            lst[c].append(L-y + 3*L)
        elif y == 0:
            lst[c].append(x)
        elif x == L:
            lst[c].append(y+L)
        elif y == L:
            lst[c].append(L-x + 2*L)
    
    dots = []
    for i in range(1, N//2 + 1):
        if len(lst[i]) != 2:
            continue
        dots.append((lst[i][1], i))
        dots.append((lst[i][0], i))
    
    
    dots.sort()
    st = []
    for i, c in dots:
        if not st or st[-1][1] != c:
            st.append((i, c))
        else:
            st.pop()
    
    
    print("1%" if not st else "0%")


solve()

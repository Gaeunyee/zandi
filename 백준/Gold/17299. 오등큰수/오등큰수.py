import sys
input = sys.stdin.readline

INF = 10**9 + 7
size = 10**6 + 1
def solve():
    N = int(input().strip())
    lst = list(map(int, input().split()))
    res = [-1]*N
    F = [0]*size
    for i in lst:
        F[i] += 1
    st = []
    for i in range(N):
        if not st or F[lst[st[-1]]] >= F[lst[i]]:
            st.append(i)
        else:
            while st and F[lst[st[-1]]] < F[lst[i]]:
                res[st[-1]] = lst[i]
                st.pop()
            st.append(i)
    print(*res)

solve()


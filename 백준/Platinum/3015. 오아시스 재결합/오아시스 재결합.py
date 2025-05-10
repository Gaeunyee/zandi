import sys
input = sys.stdin.readline


def solve():
    N = int(input().strip())
    st = []
    res = 0
    for i in range(N):
        n = int(input().strip())
        if st and st[-1][0] > n:
            res += i - st[-1][1]
            st.append((n, i, 1))
        elif not st:
            st.append((n, i, 1))
        else:
            t = 1
            while st and st[-1][0] <= n:
                if st[-1][0] == n:
                    t += st[-1][2]
                res += st[-1][2]
                st.pop()
            res += 1 if st else 0
            st.append((n, i, t))
    print(res)

solve()


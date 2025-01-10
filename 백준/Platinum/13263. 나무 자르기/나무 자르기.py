import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
st = []
dp = [0]*N

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.s = 0


def cross(l1, l2):
    return (l2.b-l1.b)/(l1.a-l2.a)


for i in range(1, N):
    l = Line(B[i-1], dp[i-1])
    while st:
        l.s = cross(l, st[-1])
        if st[-1].s < l.s:
            break
        st.pop()
    st.append(l)

    if st[-1].s <= A[i]:
        dp[i] = st[-1].a*A[i] + st[-1].b
    else:
        start, end = 0, len(st) - 1
        while start+1 < end:
            mid = (start+end)//2
            if st[mid].s > A[i]:
                end = mid
            else:
                start = mid
        dp[i] = st[start].a*A[i]+st[start].b

print(dp[N-1])

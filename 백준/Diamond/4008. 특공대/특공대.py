import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
a, b, c = map(int, input().split())
sp = [0] + list(map(int, input().split()))
s = 0
for i in range(1, N+1):
    sp[i] += sp[i-1]
st = deque()
dp = 0

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.s = 0


def cross(l1, l2):
    return (l2.b-l1.b)/(l1.a-l2.a)

for i in range(1, N+1):
    l = Line(-2*a*sp[i-1], a*(sp[i-1]**2) - b*sp[i-1] + dp)
    while st:
        l.s = cross(l, st[-1])
        if st[-1].s < l.s:
            break
        st.pop()
    st.append(l)
    if st[-1].s <= sp[i]:
        st = deque([l])
    else:
        while sp[i] >= st[1].s:
            st.popleft()

    dp = st[0].a * sp[i] + st[0].b + a * (sp[i] ** 2) + b * sp[i] + c


print(dp)
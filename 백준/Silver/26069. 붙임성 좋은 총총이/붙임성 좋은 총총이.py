import sys
input = sys.stdin.readline

N = int(input().strip())
st = {'ChongChong'}
for _ in range(N):
    a, b = input().split()
    if a in st:
        st.add(b)
    if b in st:
        st.add(a)

print(len(st))

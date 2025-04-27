import sys
input = sys.stdin.readline

N = int(input().strip())
st = set()
res = 0
for _ in range(N):
    s = input().strip()
    if s == "ENTER":
        res += len(st)
        st = set()
    else:
        st.add(s)

res += len(st)
print(res)

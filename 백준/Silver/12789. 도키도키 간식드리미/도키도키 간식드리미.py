import sys
input = sys.stdin.readline


N = int(input().strip())
lst = list(map(int, input().split()))
st = []
idx = 1
for i in lst:
    while st and st[-1] == idx:
        idx += 1
        st.pop()
    if i == idx:
        idx += 1
        continue
    else:
        st.append(i)

while st and st[-1] == idx:
    idx += 1
    st.pop()

if idx == N+1:
    print("Nice")
else:
    print("Sad")

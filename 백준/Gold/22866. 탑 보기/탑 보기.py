import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
st = []
data = [[0, -1] for _ in range(N)]
for i in range(N):
    while st and lst[st[-1]] <= lst[i]:
        st.pop()
    if st:
        data[i][0] += len(st)
        data[i][1] = st[-1]
    st.append(i)
st = []
for i in range(N-1, -1, -1):
    while st and lst[st[-1]] <= lst[i]:
        st.pop()
    if st:
        data[i][0] += len(st)
        if data[i][1] == -1 or abs(i-data[i][1]) > abs(i-st[-1]):
            data[i][1] = st[-1]
    st.append(i)
for i, j in data:
    print(i, (j+1) if i != 0 else '')


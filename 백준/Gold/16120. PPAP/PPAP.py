import sys
input = sys.stdin.readline

l = input().strip()
p = 'PPAP'
st = []
for i in l:
    while st and p[st[-1]+1] == i and st[-1] == 2:
        if st[-1] == 2:
            st.pop()
            st.pop()
            st.pop()
    if i == 'P':
        if st and st[-1] >= 0:
            st.append(1)
        else:
            st.append(0)
    else:
        if st and p[st[-1]+1] == i:
            st.append(2)
        else:
            st.append(-1)


print('PPAP' if st == [0] else 'NP')

import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    st = []
    string = input().strip()
    ok = 1
    for i in string:
        if i == '(':
            st.append('(')
        else:
            if st:
                st.pop()
            else:
                ok = 0
                break
    if ok and not st:
        print("YES")
    else:
        print("NO")




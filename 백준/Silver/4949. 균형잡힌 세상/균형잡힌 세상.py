import sys
input = sys.stdin.readline

while True:
    st = []
    string = input().rstrip()
    if string == '.':
        break
    ok = 1
    for i in string:
        if i == '(':
            st.append('(')
        elif i == '[':
            st.append('[')
        elif i == ')':
            if st and st[-1] == '(':
                st.pop()
            else:
                ok = 0
                break
        elif i == ']':
            if st and st[-1] == '[':
                st.pop()
            else:
                ok = 0
                break
    if ok and not st:
        print("yes")
    else:
        print("no")




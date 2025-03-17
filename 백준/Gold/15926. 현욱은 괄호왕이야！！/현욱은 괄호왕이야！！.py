import sys
input = sys.stdin.readline


N = int(input().strip())
l = input().strip()
st = []
tmp = []
s = []
cnt = 0
res = 0
for i in l:
    if i == '(':
        if cnt > 0:
            st.append(tmp)
            s.append(cnt)
            tmp = []
            cnt = 0
        tmp.append(i)
    else:
        if tmp:
            tmp.pop()
            cnt += 1
            if not tmp:
                if st:
                    tmp = st.pop()
                    cnt += s.pop()
            res = max(res, cnt)
        else:
            cnt = 0
            st, tmp = [], []

print(res*2)

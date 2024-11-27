import sys
input = sys.stdin.readline
INF = 10**6
N = int(input().strip())
st, ed = [-2*10**9+7], [-2*10**9+7]
cmd = []
for _ in range(N):
    a, b = map(int, input().split())
    st.append(a-b)
    ed.append(a+b)
    cmd.append((a-b, a+b))
st.append(2*10**9+7)
ed.append(2*10**9+7)
st.sort()
ed.sort()
def binarySearch1(key):
    l, r = 0, N+1 # l은 key보다 작거나 같음, r은 큼
    while l+1 < r:
        mid = (l+r)//2
        if st[mid] <= key:
            l = mid
        else:
            r = mid
    return r-1

def binarySearch2(key):
    l, r = 0, N+1 # l은 key보다 작거나 같음
    while l+1 < r:
        mid = (l+r)//2
        if ed[mid] < key:
            l = mid
        else:
            r = mid
    return l+1

for i, j in cmd:
    print(binarySearch2(i), binarySearch1(j))

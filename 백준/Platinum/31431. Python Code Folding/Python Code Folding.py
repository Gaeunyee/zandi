import sys
from math import ceil, log
input = sys.stdin.readline

N, Q = map(int, input().split())


block = [(-1, 0)]


cnt = 0
st = [(-1, 0, 0)] # 띄쓰, 타입, in
visible = N
for _ in range(N):
    l, t = input().split()
    l = int(l)
    t = 1 if t == 'h' else 0
    if l == 0 and t == 0:
        continue
    while l < st[-1][0]:
        size = 0
        while not st[-1][1]:
            size += 1
            st.pop()
        block[st[-1][2]] = (cnt, size)
        st.pop()
    if t:
        cnt += 1
        block.append((0, 0))
    st.append((l, t, cnt))
    if t:
        st.append((l+1, 0, cnt))
while st and 0 < st[-1][0]:
    size = 0
    while not st[-1][1]:
        size += 1
        st.pop()
    block[st[-1][2]] = (cnt, size)
    st.pop()

B = len(block)
H = ceil(log(B, 2))
treeSize = pow(2, H+1)
tree = [0]*(treeSize+1)
startIndex = treeSize // 2
for i in range(B):
    tree[startIndex+i] = block[i][1]

for i in range(startIndex+B, 0, -1):
    tree[i//2] += tree[i]



def editTree(i, new):
    while i != 0:
        tree[i] += new
        i //= 2


def getSum(start, end):
    res = 0
    while start <= end:
        if start % 2 == 1:
            res += tree[start]
            start += 1
        if end % 2 == 0:
            res += tree[end]
            end -= 1
        start, end = start//2, end//2
    return res


isFold = [0]*B
for _ in range(Q):
    cmd, *x = input().split()
    if cmd == 'p':
        print(visible)

    else:
        b = int(x[0])
        if not isFold[b]:
            rest = getSum(startIndex+b, startIndex+block[b][0])
            visible += -rest + 1
            editTree(startIndex+b, -rest+1)
            isFold[b] = 1

        else:
            visible += block[b][1] - tree[startIndex + b]
            editTree(startIndex + b, block[b][1]-tree[startIndex+b])
            isFold[b] = 0





import sys
input = sys.stdin.readline

N, M, U, V = map(int, input().split())
lst = list(map(lambda x: int(x)*U + V, input().split()))
s = [0]*(N*4)

tree = [0]*(N*4)
pSum, sSum = [0]*(N*4), [0]*(N*4)
def s_init(idx, l, r):
    if l == r:
        s[idx] = lst[l]
        return
    s_init(idx*2, l, (l+r)//2)
    s_init(idx*2+1, (l+r)//2+1, r)
    s[idx] = s[idx*2]+s[idx*2+1]
def s_edit(idx, a, b, l, r):
    if a < l or r < a:
        return
    if l == r:
        lst[l] = U*b + V
        s[idx] = lst[l]
        return

    s_edit(idx*2, a, b, l, (l+r)//2)
    s_edit(idx*2+1, a, b, (l+r)//2+1, r)
    s[idx] = s[idx*2]+s[idx*2+1]


def init(idx, l, r):
    if l == r:
        tree[idx], pSum[idx], sSum[idx] = lst[l], lst[l], lst[l]
        return
    init(idx*2, l, (l+r)//2)
    init(idx*2+1, (l+r)//2+1, r)
    pSum[idx] = max(pSum[idx*2], s[idx*2] + pSum[idx*2+1])
    sSum[idx] = max(sSum[idx*2+1], s[idx*2+1] + sSum[idx*2])
    tree[idx] = max(sSum[idx*2] + pSum[idx*2+1], tree[idx*2], tree[idx*2+1])

def edit(idx, e, b, l, r):
    if e < l or r < e:
        return
    if l == r:
        tree[idx], pSum[idx], sSum[idx] = b*U+V, b*U+V, b*U+V
        return
    edit(idx*2, e, b, l, (l+r)//2)
    edit(idx*2+1, e, b, (l+r)//2+1, r)
    pSum[idx] = max(pSum[idx*2], s[idx*2]+pSum[idx*2+1])
    sSum[idx] = max(sSum[idx*2+1], s[idx*2+1]+sSum[idx*2])
    tree[idx] = max(sSum[idx*2] + pSum[idx*2+1], tree[idx*2], tree[idx*2+1])
def find(idx, l, r, st, ed):  # sum, psum, ssum
    if r < st or l > ed:
        return -10**9, -10**9, -10**9
    if st <= l and r <= ed:
        return tree[idx], pSum[idx], sSum[idx]
    s1, p1, f1 = find(idx*2, l, (l+r)//2, st, ed)
    s2, p2, f2 = find(idx*2+1, (l+r)//2+1, r, st, ed)
    return max(s1, s2, f1+p2), max(p1, s[idx*2]+p2), max(f2, s[idx*2+1]+f1)


s_init(1, 0, N-1)
init(1, 0, N-1)
for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        print(find(1, 0, N-1, a-1, b-1)[0]-V)
    else:
        s_edit(1, a-1, b, 0, N-1)
        edit(1, a-1, b, 0, N-1)




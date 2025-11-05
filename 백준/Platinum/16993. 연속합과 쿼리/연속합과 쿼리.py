import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
s = [lst[0]]
for i in range(1, N):
    s.append(s[-1]+lst[i])
s.append(0)

tree = [0]*(N*4)
pSum, sSum = [0]*(N*4), [0]*(N*4)

def init(idx, l, r):
    if l == r:
        tree[idx], pSum[idx], sSum[idx] = lst[l], lst[l], lst[l]
        return
    init(idx*2, l, (l+r)//2)
    init(idx*2+1, (l+r)//2+1, r)
    pSum[idx] = max(pSum[idx*2], s[(l+r)//2]-s[l-1]+pSum[idx*2+1])
    sSum[idx] = max(sSum[idx*2+1], s[r]-s[(l+r)//2]+sSum[idx*2])
    tree[idx] = max(sSum[idx*2] + pSum[idx*2+1], tree[idx*2], tree[idx*2+1])

def find(idx, l, r, st, ed):  # sum, psum, ssum
    if r < st or l > ed:
        return -10**9, -10**9, -10**9
    if st <= l and r <= ed:
        return tree[idx], pSum[idx], sSum[idx]
    s1, p1, f1 = find(idx*2, l, (l+r)//2, st, ed)
    s2, p2, f2 = find(idx*2+1, (l+r)//2+1, r, st, ed)
    return max(s1, s2, f1+p2), max(p1, s[(l+r)//2]-s[l-1]+p2), max(f2, s[r]-s[(l+r)//2]+f1)

init(1, 0, N-1)
for _ in range(M):
    a, b = map(int, input().split())
    print(find(1, 0, N-1, a-1, b-1)[0])




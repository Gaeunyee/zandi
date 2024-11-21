import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
stu = list(map(int, input().split()))
tch = list(map(int, input().split()))
stu.sort()
tch.sort(reverse=True)
min_p = (10**9) * 2 + 5
for i in range(N):
    if i < M:
        tmp = stu[i] + tch[i]
    else:
        tmp = stu[i]
    if tmp < min_p:
        min_p = tmp

tch_idx = 0
for i in range(N):
    while tch_idx < M:
        if tch[tch_idx] + stu[i] < min_p:
            stu[i] = tch_idx
            break
        tch_idx += 1
    if tch_idx == M:
        if stu[i] >= min_p:
            stu[i] = -1
        else:
            stu[i] = M
res = 1
for i in range(N):
    if stu[i] != -1:
        res *= (stu[i] - i)
        res %= 10**9 + 7
    else:
        st = 1
        tmp = 1
        att = 1
        for k in range(N-i, max(0, N-i-(M-i)), -1):
            tmp *= ((N-i)-att+1) * ((M-i)-att+1)
            tmp //= att
            st += tmp
            att += 1
        res *= st
        res %= 10**9 + 7
        break
print(res)




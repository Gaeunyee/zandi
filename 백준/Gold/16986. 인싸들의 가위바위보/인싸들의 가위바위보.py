import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
judge = []
for _ in range(N):
    judge.append(list(map(int, input().split())))

lst = [[]]
for _ in range(2):
    lst.append(list(map(lambda x: int(x)-1, input().split())))

trace = 0
cnt = [0, -1, -1]
win_cnt = [0, 0, 0]

ok = 0
def backTrack(a, b):
    global trace, ok
    if a*b != 0:
        cnt[a] += 1
        cnt[b] += 1
        if judge[lst[a][cnt[a]]][lst[b][cnt[b]]] == 2: # 앞이 이김
            w = a
        elif judge[lst[a][cnt[a]]][lst[b][cnt[b]]] == 1:
            w = max(a, b)
        else:
            w = b
        if win_cnt[w] == K-1:
            cnt[a] -= 1
            cnt[b] -= 1
            return
        win_cnt[w] += 1
        backTrack(w, 0)
        win_cnt[w] -= 1
        cnt[a] -= 1
        cnt[b] -= 1
    elif a == 0:
        for i in range(N):
            if trace & (1 << i):
                continue
            trace |= 1<<i
            cnt[b] += 1
            if judge[i][lst[b][cnt[b]]] == 2:
                if win_cnt[a] == K-1:
                    ok = 1
                    cnt[b] -= 1
                    trace ^= 1 << i
                    return
                win_cnt[a] += 1
                backTrack(a, 3^b)
                win_cnt[a] -= 1
            else:
                if win_cnt[b] == K-1:
                    cnt[b] -= 1
                    trace ^= 1 << i
                    continue
                win_cnt[b] += 1
                backTrack(b, 3^b)
                win_cnt[b] -= 1
            cnt[b] -= 1
            trace ^= 1 << i
    else:
        for i in range(N):
            if trace & (1 << i):
                continue
            trace |= 1 << i
            cnt[a] += 1
            if judge[lst[a][cnt[a]]][i] >= 1:
                if win_cnt[a] == K-1:
                    cnt[a] -= 1
                    trace ^= 1 << i
                    continue
                win_cnt[a] += 1
                backTrack(a, 3 ^ a)
                win_cnt[a] -= 1
            else:
                if win_cnt[b] == K-1:
                    ok = 1
                    cnt[a] -= 1
                    trace ^= 1 << i
                    return
                win_cnt[b] += 1
                backTrack(b, 3 ^ a)
                win_cnt[b] -= 1
            cnt[a] -= 1
            trace ^= 1 << i


backTrack(0, 1)
print(ok)



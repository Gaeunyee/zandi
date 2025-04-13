import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
INF = 10 ** 6
size = 97

S = input().strip()
T = input().strip()
line = T+T

lst = [[] for _ in range(27)]
for i in range(len(T)*2):
    lst[ord(line[i])-97].append(i)

idx = -1
res = 0
for i in range(len(S)):
    s = ord(S[i])-97
    if not lst[s]:
        print(-1)
        exit()
    nxt = lst[s][bisect_right(lst[s], idx)]
    res += nxt-idx
    idx = nxt
    idx %= len(T)

print(res//len(T) if res % len(T) == 0 else res//len(T)+1)



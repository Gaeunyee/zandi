import sys
from collections import deque
input = sys.stdin.readline

lst = [[] for _ in range(101)]
qu = deque()
qu.append([1])
count = 0
while qu and count < 100:
    tmp = qu.popleft()
    s = tmp[-1]
    if not lst[s]:
        lst[s] = tmp
        count += 1
    for i in range(len(tmp)):
        t = tmp[i] + tmp[-1]
        if t not in tmp and t < 101:
            qu.append(tmp + [t])

while True:
    N = int(input().strip())
    if N == 0:
        break
    print(*lst[N])




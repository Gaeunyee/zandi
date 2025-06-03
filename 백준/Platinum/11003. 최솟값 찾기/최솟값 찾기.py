import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())

l = list(map(int, input().split()))
qu = deque()

for i in range(N):
    while qu and l[qu[-1]] >= l[i]:
        qu.pop()
    qu.append(i)
    while qu and i-qu[0] >= L:
        qu.popleft()
    print(l[qu[0]], end=' ')



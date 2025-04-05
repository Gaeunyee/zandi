import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n = int(input().strip())
    qu = deque(i for i in range(1, n+1))
    while len(qu) > 1:
        qu.popleft()
        qu.append(qu.popleft())
    print(qu[0])


solve()

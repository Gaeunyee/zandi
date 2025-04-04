import sys
from heapq import *
from collections import deque
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    hq = []
    for _ in range(N):
        heappush(hq, deque(input().strip().ljust(1000, '^')))

    res = []
    while hq:
        letter = heappop(hq)
        res.append(letter.popleft())
        letter.append('^')
        if letter[0] != '^':
            heappush(hq, letter)

    print(''.join(res))
solve()

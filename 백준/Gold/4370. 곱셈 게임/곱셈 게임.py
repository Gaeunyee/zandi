import sys
from math import ceil
input = sys.stdin.readline

while True:
    N = input().strip()
    if not N:
        break
    N = int(N)
    t = 1
    while N > 1:
        if t == 1:
            N = ceil(N/9)
        else:
            N = ceil(N/2)
        t *= -1
    print('Baekjoon' if t == -1 else 'Donghyuk', 'wins.')
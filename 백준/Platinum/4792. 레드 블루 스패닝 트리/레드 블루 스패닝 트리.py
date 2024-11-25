import sys
from heapq import *
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a, par):
    if par[a] == a:
        return a
    par[a] = find(par[a], par)
    return par[a]


def union(a, b, par):
    x = find(a, par)
    y = find(b, par)
    if x != y:
        if x < y:
            par[x] = y
        elif x > y:
            par[y] = x
        return 1
    return 0


def solve():
    n, m, k = map(int, input().split())
    if n == m == k == 0:
        return -1
    red_pri = []
    blue_pri = []
    for _ in range(m):
        c, a, b = input().split()
        if c == "B":
            heappush(red_pri, (2, int(a), int(b)))
            heappush(blue_pri, (1, int(a), int(b)))
        if c == "R":
            heappush(red_pri, (1, int(a), int(b)))
            heappush(blue_pri, (2, int(a), int(b)))
    counter = 0
    b_counter1 = 0
    par = [i for i in range(n + 1)]
    while counter < n-1:
        d, a, b = heappop(red_pri)
        if union(a, b, par):
            counter += 1
            if d == 2:
                b_counter1 += 1
    counter = 0
    b_counter2 = 0
    par = [i for i in range(n + 1)]
    while counter < n-1:
        d, a, b = heappop(blue_pri)
        if union(a, b, par):
            counter += 1
            if d == 1:
                b_counter2 += 1
    if b_counter2 >= k >= b_counter1:
        print(1)
    else:
        print(0)
    return


while True:
    if solve() == -1:
        break

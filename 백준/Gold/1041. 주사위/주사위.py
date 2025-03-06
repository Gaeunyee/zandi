import sys
from heapq import *
INF = 1 << 64 - 1
input = sys.stdin.readline

N = int(input().strip())
dice = list(map(int, input().split()))
arr3 = [(0, 1, 2), (0, 2, 4), (0, 4, 3), (0, 1, 3), (5, 1, 2), (5, 2, 4), (5, 4, 3), (5, 1, 3)]
arr2 = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 4), (4, 3), (3, 1),
        (5, 1), (5, 2), (5, 3), (5, 4)]

sum3 = [(dice[arr3[i][0]]+dice[arr3[i][1]]+dice[arr3[i][2]]) for i in range(8)]
sum2 = [(dice[arr2[i][0]]+dice[arr2[i][1]]) for i in range(12)]


if N == 1:
    print(sum(dice)-max(dice))
elif N == 2:
    print(min(sum3)*4+min(sum2)*4)
else:
    print(min(sum3)*4+min(sum2)*(8*N-12)+min(dice)*(5*N**2-16*N+12))



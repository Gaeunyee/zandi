import sys
input = sys.stdin.readline

#sys.setrecursionlimit(10**5)
INF = 10 ** 6

N = int(input().strip())
line = list(map(int, input().split()))
res = [0]*22
for i in line:
    for j in range(22):
        if i & (1<<j):
            res[j] += 1

print(max(res))




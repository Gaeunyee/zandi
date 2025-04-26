import sys
input = sys.stdin.readline


N = int(input().strip())
lst = [0]*10001
for i in range(N):
    lst[int(input().strip())] += 1

for i in range(1, 10001):
    for j in range(lst[i]):
        print(i)
        
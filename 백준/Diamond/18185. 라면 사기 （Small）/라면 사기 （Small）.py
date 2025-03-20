import sys
input = sys.stdin.readline


N = int(input().strip())
lst = list(map(int, input().split())) + [0, 0]
cost = 0
for i in range(N):
    if lst[i+1] > lst[i+2]:
        d = min(lst[i], lst[i+1]-lst[i+2])
        lst[i] -= d
        lst[i+1] -= d
        cost += d*5
    d = min(lst[i], lst[i+1], lst[i+2])
    lst[i] -= d
    lst[i+1] -= d
    lst[i+2] -= d
    cost += d*7 + lst[i]*3

print(cost)


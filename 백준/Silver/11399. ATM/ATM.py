import sys
input = sys.stdin.readline


N = int(input().strip())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
res = 0
for i in range(N):
    res += (i+1)*lst[i]
print(res)

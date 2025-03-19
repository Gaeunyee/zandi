import sys
input = sys.stdin.readline


N = int(input().strip())
arr = list(map(int, input().split()))
z = [(arr[i], i) for i in range(N)]
z.sort()

r = [(z[j][1], j) for j in range(N)]
r.sort()

for i in range(N):
    print(r[i][1], end=' ')

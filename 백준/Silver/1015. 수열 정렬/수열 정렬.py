import sys
input = sys.stdin.readline


N = int(input().strip())
arr = list(map(int, input().split()))
z = [(i, arr[i]) for i in range(N)]
z.sort(key=lambda x: x[1])

r = [(j, z[j][0]) for j in range(N)]
r.sort(key=lambda x: x[1])

for i in range(N):
    print(r[i][0], end=' ')

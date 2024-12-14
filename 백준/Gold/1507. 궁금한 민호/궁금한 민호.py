import sys

input = sys.stdin.readline

N = int(input().strip())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

res = 0
isOk = 1
for i in range(N):
    for j in range(i+1, N):
        flag = 1
        for k in range(N):
            if k != i and k != j and matrix[i][j] > matrix[i][k] + matrix[k][j]:
                isOk = 0
            if k != i and k != j and matrix[i][j] == matrix[i][k] + matrix[k][j]:
                flag = 0
                break
        if flag:
            res += matrix[i][j]
if isOk:
    print(res)
else:
    print(-1)



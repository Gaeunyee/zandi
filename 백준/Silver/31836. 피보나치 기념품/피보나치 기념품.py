import sys
input = sys.stdin.readline

INF = 10**9


N = int(input().strip())

A, B = [], []
for i in range(N-2, 0, -3):
    A.append(i)
    A.append(i+1)
    B.append(i+2)

if N % 3 == 2:
    A.append(1)
    B.append(2)

print(len(A))
print(*A)
print(len(B))
print(*B)



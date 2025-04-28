import sys
input = sys.stdin.readline

N = int(input().strip())
lst = list(map(int, input().split()))
lst.sort()

M = int(input().strip())
target = list(map(int, input().split()))
query = []
for i in range(M):
    query.append((target[i], i))

query.sort()
res = [0]*M
idx = 0
for n, i in query:
    while n > lst[idx] and idx < N-1:
        idx += 1
    if lst[idx] == n:
        res[i] = 1
    else:
        res[i] = 0
for i in res:
    print(i)



import sys
input = sys.stdin.readline


N = int(input())
table = []
for _ in range(N):
    table.append(tuple(map(int, input().split())))

table = sorted(table, key=lambda x: (x[1], x[0]))
temp = -1
cnt = 0
for st, ed in table:
    if st >= temp:
        cnt += 1
        temp = ed

print(cnt)

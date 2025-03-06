import sys
input = sys.stdin.readline

arr = [0]*31
for _ in range(28):
    arr[int(input().strip())] = 1

for i in range(1, 31):
    if not arr[i]:
        print(i)


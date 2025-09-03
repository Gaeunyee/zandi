import sys
input = sys.stdin.readline

N = int(input())
F = int(input())
for i in range(10):
    if not (N//100 *100 + i)%F:
        print(f'0{i}')
        exit()

for i in range(10, 100):
    if not (N // 100 * 100 + i) % F:
        print(i)
        break


import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(1, N+1):
    u, v = map(int, input().split())
    print(f"Case #{i}: {u+v}")
import sys
input = sys.stdin.readline


N = int(input().strip())
res = 0
for i in map(int, input().split()):
    res ^= i-2

w = 1 if input().strip() == "Whiteking" else -1
if not res:
    w *= -1

print("Whiteking" if w == 1 else "Blackking")

import sys
input = sys.stdin.readline

l = input().strip()
for i in range(len(l)//2 + 1):
    if l[len(l)-1-i] != l[i]:
        print(0)
        exit()

print(1)


import sys
import math
input = sys.stdin.readline


l = input().strip()
flag = 1
for i in range(1, len(l)):
    if l[0] != l[i]:
        flag = 0
if flag:
    print(-1)
    exit()
for i in range(len(l)//2):
    if l[i] != l[len(l)-1-i]:
        print(len(l))
        exit()
print(len(l)-1)


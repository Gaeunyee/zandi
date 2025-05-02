import sys
input = sys.stdin.readline


S = input().strip()

lst = [[0]*26]
for i in range(len(S)):
    lst.append(lst[-1][:])
    lst[-1][ord(S[i])-97] += 1

Q = int(input().strip())

for _ in range(Q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    print(lst[r+1][ord(a)-97]-lst[l][ord(a)-97])



